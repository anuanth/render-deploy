from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_domain_details import Phc_domain_detailsDB

def read_Phc_domain_details_all(db: Session, user_id: int):
    try:
        phc_domain_details_list = db.query(Phc_domain_detailsDB).filter(
            Phc_domain_detailsDB.user_id == user_id
        ).all()

        return phc_domain_details_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
