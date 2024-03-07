from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.specializations import SpecializationDB

def read_Specializations(db: Session, user_id: int):
    try:
        Specializations = db.query(SpecializationDB).filter(
            SpecializationDB.user_id == user_id
        ).all()

        return Specializations

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
