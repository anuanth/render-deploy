from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#pydantic model for roles
class Create_roles(BaseModel):
    user_id: str
    roles_name : str
    status:Optional[int] = None
    
    class Config:
        orm_mode = True
    
class Roles_response(BaseModel):
    user_id: str
    roles_name : str
    status: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True