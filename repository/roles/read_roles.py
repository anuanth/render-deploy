from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.roles import RolesDB

def read_roles_all(db: Session, user_id: int):
    try:
        roles_list = db.query(RolesDB).filter(
            RolesDB.user_id == user_id
        ).all()

        return roles_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
