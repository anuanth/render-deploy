from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_domain_details import Phc_domain_detailsDB

def create_phc_domain_details(db: Session, user_id: int, phc_detail_ID: str, Domain_ID: str, remarks: str, status: str):
    try:
        db_Phc_domain_details = Phc_domain_detailsDB(
            user_id=user_id,
            phc_detail_ID=phc_detail_ID,
            Domain_ID=Domain_ID,
            remarks=remarks,
            status=status
        )

        db.add(db_Phc_domain_details)
        db.commit()
        db.refresh(db_Phc_domain_details)
        return db_Phc_domain_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
