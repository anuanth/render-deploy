from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.phc_domain_details import Phc_domain_detailsDB

def read_Phc_domain_details_by_id(db: Session, phc_domain_details_id: str, user_id: int):
    try:
        phc_domain_details = db.query(Phc_domain_detailsDB).filter(
            Phc_domain_detailsDB.id == phc_domain_details_id,
            Phc_domain_detailsDB.user_id == user_id
        ).first()
        return phc_domain_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
