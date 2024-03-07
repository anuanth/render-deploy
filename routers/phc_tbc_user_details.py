from fastapi import HTTPException, Header, APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.phc_tbc_user_details import phc_tbc_user_details_response, Create_phc_tbc_user_details
from database.database import get_db
from passlib.context import CryptContext
from routers.auth1 import get_current_user
from repository.phc_tbc_user_details import create_phc_tbc_user_detail
from repository.phc_tbc_user_details import read_phc_tbc_user_detail
from repository.phc_tbc_user_details import read_phc_tbc_user_details

router = APIRouter(prefix='/phc_tbc_user_details', tags=['phc_tbc_user_details'])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post("/phc_tbc_user_details/")
async def create_phc_tbc_user_details(phc_tbc_user_details: Create_phc_tbc_user_details, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_phc_tbc_user_detail.create_Phc_tbc_user_details(
            db,
            user_id,
            phc_tbc_user_details.phc_detail_ID,
            phc_tbc_user_details.user_name,
            bcrypt_context.hash(phc_tbc_user_details.password),
            phc_tbc_user_details.tbc_code_ID,
            phc_tbc_user_details.name,
            phc_tbc_user_details.specialization_id,
            phc_tbc_user_details.remarks,
            phc_tbc_user_details.status
        )

        return {"message": "phc_tbc_user_detail created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/phc_tbc_user_details/{phc_tbc_user_details_id}", response_model=phc_tbc_user_details_response)
async def read_Phc_Tbc_user_details_id(phc_tbc_user_details_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        phc_tbc_user_details = read_phc_tbc_user_detail.read_Phc_tbc_user_details_by_id(db, phc_tbc_user_details_id, user_id)

        if phc_tbc_user_details:
            return phc_tbc_user_details
        raise HTTPException(status_code=404, detail="phc_tbc_user_details not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/phc_tbc_user_details/", response_model=list[phc_tbc_user_details_response])
async def read_Phc_Tbc_user_details(db: Session = Depends(get_db), token: str = Header(...)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        phc_tbc_user_details = read_phc_tbc_user_details.read_phc_tbc_user_details_all(db, user_id)
        return phc_tbc_user_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
