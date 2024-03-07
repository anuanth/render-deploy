from typing import List
from fastapi import HTTPException, APIRouter, Depends,status,Header
from sqlalchemy.orm import Session
from schemas.domain import DomainCreate, DomainResponse
from database.database import get_db
from routers.auth1 import get_current_user
from repository.domains import Create_domains
from repository.domains import Read_domain
from repository.domains import Read_domains

router = APIRouter(prefix='/domain', 
                   tags=['domain'])

    
@router.post("/domains/")
async def create_domain(domain: DomainCreate, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        Create_domains.create_domains(db, user_id, domain.domain_name, domain.remarks, domain.status)

        return {"message": "domain created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
    
@router.get("/domains/{domain_id}", response_model=DomainResponse)
async def read_domain(domain_id: int, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        domain = Read_domain.read_domain_by_id(db, domain_id, user_id)

        if domain:
            return domain
        raise HTTPException(status_code=404, detail="Domain not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/domains/", response_model=List[DomainResponse])
async def read_user_domains(db: Session = Depends(get_db), token: str = Header(...)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']
        
        domains = Read_domains.read_domains(db, user_id)
        return domains

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
