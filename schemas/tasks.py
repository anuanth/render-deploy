from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#pydantic model for task
class Create_task(BaseModel):
    user_id: str
    task_name : str
    evidence_of_compliance:str
    per_visit:str
    staff_availability:str
    awareness_trained:str
    remarks:Optional[str] = None
    
    class Config:
        orm_mode = True
    
class task_response(BaseModel):
    user_id: str
    task_name : str
    evidence_of_compliance:str
    per_visit:str
    staff_availability:str
    awareness_trained:str
    remarks:Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True