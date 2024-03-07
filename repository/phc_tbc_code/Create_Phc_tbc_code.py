from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_tbc_code import Phc_tbc_codeDB

def create_Phc_tbc_code(db: Session, user_id: int, zone_ID: str, phc_detail_ID: str, tbc_code: str, remarks: str, status: str):
    try:
        db_Phc_tbc_code = Phc_tbc_codeDB(
            user_id=user_id,
            zone_ID=zone_ID,
            phc_detail_ID=phc_detail_ID,
            tbc_code=tbc_code,
            remarks=remarks,
            status=status
        )

        db.add(db_Phc_tbc_code)
        db.commit()
        db.refresh(db_Phc_tbc_code)
        return db_Phc_tbc_code

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
