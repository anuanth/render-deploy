from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.specializations import SpecializationDB

def Create_Specialization(db: Session, user_id: int, speciality_name: str, status: str):
    try:
        db_Specialization = SpecializationDB(
            user_id=user_id,
            speciality_name=speciality_name,
            status=status
        )

        db.add(db_Specialization)
        db.commit()
        db.refresh(db_Specialization)
        return db_Specialization

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
