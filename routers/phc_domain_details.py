from fastapi import HTTPException, APIRouter, Depends, status, Header
from sqlalchemy.orm import Session
from schemas.phc_domain_details import Phc_domain_details_response, Create_Phc_domain_detail
from database.database import get_db
from routers.auth1 import get_current_user
from repository.phc_domain_details import Create_Phc_domain_details 
from repository.phc_domain_details import Read_create_Phc_domain_detail
from repository.phc_domain_details import Read_create_Phc_domain_details


router = APIRouter(prefix='/Phc_domain_details', tags=['Phc_domain_details'])

@router.post("/Phc_domain_details/")
async def create_Phc_domain_details(Phc_domain_details: Create_Phc_domain_detail, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Create_Phc_domain_details.create_phc_domain_details(db, user_id, Phc_domain_details.phc_detail_ID, Phc_domain_details.Domain_ID, Phc_domain_details.remarks, Phc_domain_details.status)

        return {"message": "db_Phc_domain_details created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Phc_domain_details/{Phc_domain_details_id}", response_model=Phc_domain_details_response)
async def read_Phc_domain_details(Phc_domain_details_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        phc_domain_details = Read_create_Phc_domain_detail.read_Phc_domain_details_by_id(db, Phc_domain_details_id, user_id)

        if phc_domain_details:
            return phc_domain_details
        raise HTTPException(status_code=404, detail="Phc_domain_details not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Phc_domain_details/", response_model=list[Phc_domain_details_response])
async def read_Phc_domain_details(db: Session = Depends(get_db), token: str = Header(...)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        phc_domain_details_list = Read_create_Phc_domain_details.read_Phc_domain_details_all(db, user_id)
        return phc_domain_details_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
