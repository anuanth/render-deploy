from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from models.domain import DomainDB

def read_domain_by_id(db: Session, domain_id: int, user_id: int):
    try:
        domain = db.query(DomainDB).filter(
            DomainDB.id == domain_id,
            DomainDB.user_id == user_id
        ).first()
        return domain
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))