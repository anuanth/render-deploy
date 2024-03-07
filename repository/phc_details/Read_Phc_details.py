from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_details import Phc_detailsDB

def read_all_phc_details(db: Session, user_id: int):
    try:
        phc_details = db.query(Phc_detailsDB).filter(
            Phc_detailsDB.user_id == user_id
        ).all()
        return phc_details
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
