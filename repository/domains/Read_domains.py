from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from models.domain import DomainDB

def read_domains(db: Session, user_id: int):
    try:
        domains = db.query(DomainDB).filter(
            DomainDB.user_id == user_id
        ).all()

        return domains

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))