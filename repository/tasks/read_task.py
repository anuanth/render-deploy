from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.tasks import TasksDB

def read_task_by_id(db: Session, tasks_id: str, user_id: int):
    try:
        tasks = db.query(TasksDB).filter(
            TasksDB.id == tasks_id,
            TasksDB.user_id == user_id
        ).first()
        return tasks

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
