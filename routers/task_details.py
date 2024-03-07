from fastapi import HTTPException, Header, APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.task_details import task_details_response, Create_Task_details
from database.database import get_db
from routers.auth1 import get_current_user
from repository.task_details import create_task_details, read_task_detail, read_task_details

router = APIRouter(prefix='/task_details', tags=['task_details'])

@router.post("/task_details/")
async def create_Task_details(Task_details: Create_Task_details, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_task_details.create_Task_details(db, user_id, Task_details)

        return {"message": "task_details created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/task_details/{task_details_id}", response_model=task_details_response)
async def Read_task_detail(task_details_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        task_details = read_task_detail.read_task_detail_by_id(db, task_details_id, user_id)

        if task_details:
            return task_details
        raise HTTPException(status_code=404, detail="Task_details not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/task_details/", response_model=list[task_details_response])
async def Read_task_details(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        task_details_list = read_task_details.read_task_details(db, user_id)
        return task_details_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
