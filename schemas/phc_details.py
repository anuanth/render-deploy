from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from schemas.zones import Zoneresponse

#pydantic model for phc_details
class Create_Phc_details(BaseModel):
    user_id: str
    phc_name: str
    zone_ID: str
    remarks:Optional[str] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True
        
class Phc_details_response(BaseModel):
    user_id: str
    phc_name: Optional[str] = None
    zone_ID: str
    remarks: Optional[str] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    zones:Zoneresponse
    
    class Config:
        orm_mode = True
        

        
        
