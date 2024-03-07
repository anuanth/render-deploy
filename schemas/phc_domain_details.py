from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from schemas.domain import DomainResponse
from schemas.phc_details import Phc_details_response

#pydantic model for phc_domain_details
class Create_Phc_domain_detail(BaseModel):
    user_id: str
    phc_detail_ID: Optional[int] = None
    Domain_ID: Optional[int] = None
    remarks: str
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

        
class Phc_domain_details_response(BaseModel):
    user_id: str
    phc_detail_ID: Optional[int] = None
    Domain_ID : Optional[int] = None
    remarks:Optional[str] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    domains:DomainResponse
    
    phc_details:Phc_details_response
    
    
   

    class Config:
        orm_mode = True
        


        

    
