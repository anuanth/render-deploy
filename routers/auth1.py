from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from starlette import status
from typing import Annotated
from database.database import get_db
from models.users import UsersDB
from jose import JWTError,jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from schemas.user import CreateUserRequest, Token
import uuid

router = APIRouter(
  prefix='/auth1',
  tags=['auth1']
)

SECRET_KEY = "cf409ca9d9836cbfbb5a39187348e29621bb7c059707f341584ad7cd27a056b9"
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth1/token')

db_dependency = Annotated[Session,Depends(get_db)]


@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    try:
      create_user_model = UsersDB(
      name=create_user_request.name,
      password=bcrypt_context.hash(create_user_request.password),
      email=create_user_request.email,
      status=create_user_request.status,
      remember_token = create_user_request.remember_token

    )

      db.add(create_user_model)
      db.commit()
      db.refresh(create_user_model)
      
      return {"message": "User created successfully"}
    
    except Exception as e:
      return str(e)
   
  

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
  
  try:
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='could not validate user')
    token = create_access_token(user.name,user.id,timedelta(minutes=30))
  
    return {'access_token':token, 'token_type':'bearer'}
  except Exception as e:
        return {'error': str(e)}
  
def authenticate_user(name: str, password: str, db: Session):
    try:
        user = db.query(UsersDB).filter(UsersDB.name == name).first()

        if not user or not bcrypt_context.verify(password, user.password):
            return False

        return user

    except Exception as e:
        return {'error':str()}



def create_access_token(name: str, user_id: int, expires_delta: timedelta):
    try:
        encode = {'sub': name, 'id': user_id}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    except Exception as e:
        return {'error': str(e)}

def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        name: str = payload.get('sub')
        user_id: int = payload.get('id')
        if name is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user')
        return {'name': name, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user')



  
user_dependency = Depends(get_current_user)


@router.get("/", status_code=status.HTTP_200_OK)
async def user_handler(token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        return user_info
    except Exception as e:
        return str(e)

