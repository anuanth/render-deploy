from fastapi import HTTPException, Header, APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.phc_tbc_code import Phc_tbc_code_response, Create_Phc_tbc_codes
from database.database import get_db
from routers.auth1 import get_current_user
from repository.phc_tbc_code import Create_Phc_tbc_code
from repository.phc_tbc_code import Read_Phc_tbc_code
from repository.phc_tbc_code import Read_Phc_tbc_codes

router = APIRouter(prefix='/Phc_tbc_code', tags=['Phc_tbc_code'])

@router.post("/Phc_tbc_code/")
async def create_Phc_tbc_code(Phc_tbc_code: Create_Phc_tbc_codes, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Create_Phc_tbc_code.create_Phc_tbc_code(db, user_id, Phc_tbc_code.zone_ID, Phc_tbc_code.phc_detail_ID, Phc_tbc_code.tbc_code, Phc_tbc_code.remarks, Phc_tbc_code.status)

        return {"message": "phc_tbc_code created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Phc_tbc_code/{Phc_tbc_code_id}", response_model=Phc_tbc_code_response)
async def read_Phc_tbc_code(Phc_tbc_code_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Phc_tbc_code = Read_Phc_tbc_code.read_Phc_tbc_code_by_id(db, Phc_tbc_code_id, user_id)

        if Phc_tbc_code:
            return Phc_tbc_code
        raise HTTPException(status_code=404, detail="Phc_tbc_code not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/Phc_tbc_code/", response_model=list[Phc_tbc_code_response])
async def read_Phc_tbc_codes(db: Session = Depends(get_db), token: str = Header(...)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Phc_tbc_codes = Read_Phc_tbc_codes.read_Phc_tbc_codes_all(db, user_id)
        return Phc_tbc_codes

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
