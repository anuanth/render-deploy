from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from models.domain import DomainDB

def create_domains(db: Session, user_id: int, domain_name: str, remarks: str, status: str):
    try:
      db_domain = DomainDB(
        user_id=user_id,
        domain_name=domain_name,
        remarks=remarks,
        status=status
      )

      db.add(db_domain)
      db.commit()
      db.refresh(db_domain)
      return db_domain
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))