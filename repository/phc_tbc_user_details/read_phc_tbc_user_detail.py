from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.phc_tbc_user_details import Phc_tbc_user_detailsDB

def read_Phc_tbc_user_details_by_id(db: Session, phc_tbc_user_details_id: str, user_id: int):
    try:
        phc_tbc_user_details = db.query(Phc_tbc_user_detailsDB).filter(
            Phc_tbc_user_detailsDB.id == phc_tbc_user_details_id,
            Phc_tbc_user_detailsDB.user_id == user_id
        ).first()
        return phc_tbc_user_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
