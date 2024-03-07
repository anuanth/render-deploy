from pydantic import BaseModel
from typing import  Optional
from datetime import datetime
from schemas.zones import Zoneresponse
from schemas.phc_details import Phc_details_response
 

#pydantic model for phc_tbc_code
class Create_Phc_tbc_codes(BaseModel):
    user_id: str
    zone_ID : Optional[int] = None
    phc_detail_ID:Optional[int] = None
    tbc_code : str
    remarks:Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True
    
class Phc_tbc_code_response(BaseModel):
    user_id: str
    zone_ID : Optional[int] = None
    phc_detail_ID:Optional[int] = None
    tbc_code : str
    remarks:Optional[str] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    zones:Zoneresponse
    
    phc_details:Phc_details_response
    
    class Config:
        orm_mode = True

        