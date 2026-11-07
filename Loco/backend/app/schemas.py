from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str = ""
    city_town: str = ""
    country: str = ""

class UserCreate(UserBase):
    password: str
    role: str = "user"  

class UserResponse(UserBase):
    uid: int
    role: str
    is_active: bool

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str