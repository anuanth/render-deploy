from fastapi import HTTPException, Header, APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.roles import Roles_response, Create_roles
from database.database import get_db
from models.roles import RolesDB
from routers.auth1 import get_current_user
from repository.roles import create_roles
from repository.roles import read_role
from repository.roles import read_roles

router = APIRouter(prefix='/roles', tags=['Roles'])

@router.post("/roles/")
async def Create_roles(Roles: Create_roles, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_roles.create_role(db, user_id, Roles.roles_name, Roles.status)

        return {"message": "roles created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/roles/{roles_id}", response_model=Roles_response)
async def Read_Roles(roles_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        roles = read_role.read_roles_by_id(db, roles_id, user_id)

        if roles:
            return roles
        raise HTTPException(status_code=404, detail="Roles not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/roles/", response_model=list[Roles_response])
async def Read_roles(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        roles_list = read_roles.read_roles_all(db, user_id)
        return roles_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
