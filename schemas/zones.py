from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#pydantic model for zone
class Newzone(BaseModel):
    user_id: str
    zone_name: str
    remarks:Optional[str] = None
    status: int = 0
    
    class Config:
        orm_mode = True

class Zoneresponse(BaseModel):
    user_id: str
    zone_name: str
    remarks: Optional[str] = None
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True