import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

JWT_SECRET = os.getenv("JWT_SECRET", "helloworld")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "43200"))
ALGORITHM = "HS256"

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=JWT_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["auth"])

# Replace with your real DB later
_FAKE_USERS = {}  # username -> password_hash

class SignupIn(BaseModel):
    username: str
    password: str

class LoginIn(BaseModel):
    username: str
    password: str

@router.post("/signup")
async def signup(body: SignupIn):
    if body.username in _FAKE_USERS:
        raise HTTPException(status_code=400, detail="User already exists")
    _FAKE_USERS[body.username] = get_password_hash(body.password)
    return {"ok": True}

@router.post("/login")
async def login(body: LoginIn):
    pw_hash = _FAKE_USERS.get(body.username)
    if not pw_hash or not verify_password(body.password, pw_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": body.username})
    return {"access_token": token, "token_type": "bearer"}

# Example protected route (optional)
@router.get("/me")
async def me(username: str = Depends(get_current_user_token)):
    return {"username": username}
