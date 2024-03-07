from pydantic import BaseModel
from typing import List,  Optional
from datetime import datetime
from schemas.phc_details import Phc_details_response
from schemas.phc_tbc_code import Phc_tbc_code_response
from schemas.specialization import Specialityresponse

#pydantic model for phc_tbc_user_details
class Create_phc_tbc_user_details(BaseModel): 
    user_id: str  
    phc_detail_ID : Optional[int] = None
    user_name:str
    password:str
    tbc_code_ID:Optional[int] = None
    name:str
    specialization_id:Optional[int] = None
    remarks:str
    status: Optional[int] = None
    
    class Config:
        orm_mode = True
        
class phc_tbc_user_details_response(BaseModel):
    user_id: str
    phc_detail_ID : Optional[int] = None
    user_name:str
    password:str
    tbc_code_ID:Optional[int] = None
    name:str
    specialization_id:Optional[int] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    phc_details : Phc_details_response
    
    phc_tbc_code : Phc_tbc_code_response
    
    specializations: Specialityresponse

    
    class Config:
        orm_mode = True

   
