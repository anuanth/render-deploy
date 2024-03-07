from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_details import Phc_detailsDB

def create_phc_details(db: Session, user_id: int, zone_ID: str, phc_name: str, remarks: str, status: str):
    try:
        db_phc_details = Phc_detailsDB(
            user_id=user_id,
            zone_ID=zone_ID,
            phc_name=phc_name,
            remarks=remarks,
            status=status
        )
        db.add(db_phc_details)
        db.commit()
        db.refresh(db_phc_details)
        return {"message": "phc_detail created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))