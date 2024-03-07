from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.task_details import Task_detailsDB

def read_task_details(db: Session, user_id: int):
    try:
        task_details_list = db.query(Task_detailsDB).filter(
            Task_detailsDB.user_id == user_id
        ).all()

        return task_details_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
