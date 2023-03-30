from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status

from .schemas.user_schema import UserBase, UserIn
from .schemas.token_schema import Token, TokenData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .routes import task_router

from .services import user_service
from .dependencies import get_db
from sqlalchemy.orm import Session

# last step
from jose import JWTError, jwt
from passlib.context import CryptContext

from .utils import create_access_token, verify_password

# keys for generate a token
SECRET_KEY = "8ae4731bc228a97adb7c4df208d379a34c8536a499468f9b450a4b708e9b058d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="📑 Task API 📑",
              version="1.0",
              description="Personal task api to manage user's tasks")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


###################### dependencias
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db())):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db=db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@app.get(path="/", tags=['Root'], status_code=status.HTTP_200_OK)
def index():
    return {"Hello": "Welcome to Task API 📑"}


def get_user(username: str, db: Session = Depends(get_db)):
    """Get the user form the database"""
    user = user_service.get_user_by_username(db=db, username=username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@app.post("/auth/login", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
):
    user = authenticate_user(db=db, username=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me/", response_model=UserBase)
# def read_users_me(current_user: Annotated[UserBase, Depends(get_current_user)]):
#     return current_user


app.include_router(task_router.router, prefix="/api/v1", )
