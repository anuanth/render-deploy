from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.phc_tbc_code import Phc_tbc_codeDB

def read_Phc_tbc_code_by_id(db: Session, phc_tbc_code_id: str, user_id: int):
    try:
        phc_tbc_code = db.query(Phc_tbc_codeDB).filter(
            Phc_tbc_codeDB.id == phc_tbc_code_id,
            Phc_tbc_codeDB.user_id == user_id
        ).first()
        return phc_tbc_code

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
