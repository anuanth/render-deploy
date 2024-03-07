from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_tbc_user_details import Phc_tbc_user_detailsDB

def create_Phc_tbc_user_details(
    db: Session, user_id: int, phc_detail_ID: str, user_name: str,
    password: str, tbc_code_ID: str, name: str, specialization_id: int,
    remarks: str, status: str
):
    try:
        db_phc_tbc_user_details = Phc_tbc_user_detailsDB(
            user_id=user_id,
            phc_detail_ID=phc_detail_ID,
            user_name=user_name,
            password=password,
            tbc_code_ID=tbc_code_ID,
            name=name,
            specialization_id=specialization_id,
            remarks=remarks,
            status=status
        )

        db.add(db_phc_tbc_user_details)
        db.commit()
        db.refresh(db_phc_tbc_user_details)
        return db_phc_tbc_user_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
