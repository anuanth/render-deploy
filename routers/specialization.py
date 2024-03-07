from fastapi import HTTPException, Header, APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.specialization import Specialityresponse, Newspeciality
from database.database import get_db
from routers.auth1 import get_current_user
from repository.specialization import create_Specialization, read_Specialization, read_Specializations

router = APIRouter(prefix='/Specialization', tags=['Specialization'])

@router.post("/Specialization/")
async def create_Specializations(Specialization: Newspeciality, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_Specialization.Create_Specialization(db, user_id, Specialization.speciality_name, Specialization.status)

        return {"message": "specialization created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Specialization/{Specialization_id}", response_model=Specialityresponse)
async def Read_Specialization(Specialization_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Specialization = read_Specialization.read_Specialization_by_id(db, Specialization_id, user_id)

        if Specialization:
            return Specialization
        raise HTTPException(status_code=404, detail="Specialization not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Specialization/", response_model=list[Specialityresponse])
async def Read_Specializations(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Specializations = read_Specializations.read_Specializations(db, user_id)
        return Specializations

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
