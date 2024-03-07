from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.roles import RolesDB

def read_roles_by_id(db: Session, roles_id: str, user_id: int):
    try:
        roles = db.query(RolesDB).filter(
            RolesDB.id == roles_id,
            RolesDB.user_id == user_id
        ).first()
        return roles

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
