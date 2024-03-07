from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_tbc_user_details import Phc_tbc_user_detailsDB

def read_phc_tbc_user_details_all(db: Session, user_id: int):
    try:
        phc_tbc_user_details = db.query(Phc_tbc_user_detailsDB).filter(
            Phc_tbc_user_detailsDB.user_id == user_id
        ).all()

        return phc_tbc_user_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
