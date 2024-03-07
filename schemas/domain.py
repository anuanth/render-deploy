from pydantic import BaseModel
from typing import  Optional
from datetime import datetime

#pydantic model for domain
class DomainCreate(BaseModel):
    user_id: str
    domain_name: str
    remarks: Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True
    

class DomainResponse(BaseModel):
    
    user_id: str
    domain_name: str
    remarks: Optional[str] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
