from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.specializations import SpecializationDB

def read_Specialization_by_id(db: Session, Specialization_id: str, user_id: int):
    try:
        Specialization = db.query(SpecializationDB).filter(
            SpecializationDB.id == Specialization_id,
            SpecializationDB.user_id == user_id
        ).first()
        return Specialization

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
