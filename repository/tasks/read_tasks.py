from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.tasks import TasksDB

def read_tasks(db: Session, user_id: int):
    try:
        tasks_list = db.query(TasksDB).filter(
            TasksDB.user_id == user_id
        ).all()

        return tasks_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
