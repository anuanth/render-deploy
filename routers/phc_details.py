from typing import List
from fastapi import HTTPException, APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.phc_details import Phc_details_response, Create_Phc_details
from database.database import get_db
from routers.auth1 import get_current_user
from fastapi import Header
from repository.phc_details import Create_Phc_detail
from repository.phc_details import Read_Phc_detail
from repository.phc_details import Read_Phc_details

router = APIRouter(prefix='/Phc_details', tags=['Phc_details'])

@router.post("/Phc_details/")
async def create_Phc_details(phc_details: Create_Phc_details, db: Session = Depends(get_db), token: str = Header(...)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']
        Create_Phc_detail.create_phc_details(db, user_id, phc_details.zone_ID, phc_details.phc_name, phc_details.remarks, phc_details.status)
        return {"message": "phc_detail created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/Phc_details/{Phc_details_id}", response_model=Phc_details_response)
async def read_Phc_details(Phc_details_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']
        phc_details = Read_Phc_detail.read_phc_details_by_id(db, Phc_details_id, user_id)
        if phc_details:
            return phc_details
        raise HTTPException(status_code=404, detail="Phc_details not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/Phc_details/", response_model=List[Phc_details_response])
async def read_all_Phc_details(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']
        phc_details = Read_Phc_details.read_all_phc_details(db, user_id)
        return phc_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
