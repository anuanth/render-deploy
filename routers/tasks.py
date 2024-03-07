from fastapi import HTTPException, APIRouter, Depends, Header, status
from sqlalchemy.orm import Session
from schemas.tasks import task_response, Create_task
from database.database import get_db
from models.tasks import TasksDB
from routers.auth1 import get_current_user
from repository.tasks import create_tasks, read_task, read_tasks

router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.post("/tasks/")
async def create_Tasks(tasks: Create_task, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_tasks.Create_tasks(db, user_id, tasks)

        return {"message": "task created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/tasks/{tasks_id}", response_model=task_response)
async def read_Task(tasks_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        tasks = read_task.read_task_by_id(db, tasks_id, user_id)

        if tasks:
            return tasks
        raise HTTPException(status_code=404, detail="Tasks not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/tasks/", response_model=list[task_response])
async def read_Tasks(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        tasks_list = read_tasks.read_tasks(db, user_id)
        return tasks_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
