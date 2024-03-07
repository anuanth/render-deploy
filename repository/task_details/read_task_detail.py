from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.task_details import Task_detailsDB

def read_task_detail_by_id(db: Session, task_details_id: str, user_id: int):
    try:
        task_details = db.query(Task_detailsDB).filter(
            Task_detailsDB.id == task_details_id,
            Task_detailsDB.user_id == user_id
        ).first()
        return task_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
