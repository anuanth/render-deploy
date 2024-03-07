from pydantic import BaseModel
from typing import Optional
# pydantic model for user
class CreateUserRequest(BaseModel):
    name: str
    password: str
    email : str
    remember_token :str
    status: Optional[int] = None

    
    

#pydantic model for token
class Token(BaseModel):
  access_token:str
  token_type:str