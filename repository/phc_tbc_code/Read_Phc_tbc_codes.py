from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.phc_tbc_code import Phc_tbc_codeDB

def read_Phc_tbc_codes_all(db: Session, user_id: int):
    try:
        phc_tbc_codes = db.query(Phc_tbc_codeDB).filter(
            Phc_tbc_codeDB.user_id == user_id
        ).all()

        return phc_tbc_codes

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
