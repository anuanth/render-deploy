from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.roles import RolesDB

def create_role(db: Session, user_id: int, roles_name: str, status: str):
    try:
        db_roles = RolesDB(
            user_id=user_id,
            roles_name=roles_name,
            status=status
        )

        db.add(db_roles)
        db.commit()
        db.refresh(db_roles)
        return db_roles

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
