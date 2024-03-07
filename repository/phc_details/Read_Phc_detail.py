from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.phc_details import Phc_detailsDB

def read_phc_details_by_id(db: Session, phc_details_id: int, user_id: int):
    try:
        phc_details = db.query(Phc_detailsDB).filter(
            Phc_detailsDB.id == phc_details_id,
            Phc_detailsDB.user_id == user_id
        ).first()
        return phc_details
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))