from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#pydantic model for specializations
class Newspeciality(BaseModel):
    user_id: str
    speciality_name: str
    status: int = 0
    
    class Config:
        orm_mode = True

class Specialityresponse(BaseModel):
    user_id: str
    speciality_name: str
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True