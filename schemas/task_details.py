from pydantic import BaseModel,constr
from typing import List, Optional
from datetime import datetime,date
from schemas.tasks import task_response

#pydantic model for task details
class Create_Task_details(BaseModel):   
    user_id: str
    task_id : Optional[int] = None
    assigned_to:str
    co_assigned_to:str
    correction_action_plan:str
    dependent_days:int
    working_days:int
    start_date: date
    end_date: date
    status_progression:str
    score:int
    remarks:Optional[str] = None
    
    class Config:
        orm_mode = True

class task_details_response(BaseModel):
    user_id: str
    task_id : Optional[int] = None
    assigned_to:str
    co_assigned_to : str
    correction_action_plan:str
    dependent_days:int
    working_days : int
    start_date: date
    end_date: date
    status_progression : str
    score:int
    remarks:Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    
    tasks:task_response   
     
    class Config:
        orm_mode = True
  