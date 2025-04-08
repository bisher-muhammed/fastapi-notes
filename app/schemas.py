from pydantic import BaseModel, EmailStr,field_validator
import uuid
from datetime import datetime
from typing import Optional
import re

class UserCreate(BaseModel):
    user_name: str
    user_email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'\d', value):
            raise ValueError("Password must contain at least one number")
        return value




class UserResponse(BaseModel):
    user_id: uuid.UUID
    user_name: str
    user_email: EmailStr

    class Config:
        from_attributes = True  # Pydantic v2 (Use `orm_mode = True` for Pydantic v1)


class LoginRequest(BaseModel):
    user_email: str
    password: str

class NoteCreate(BaseModel):
    note_title: str
    note_content: str

class NoteResponse(BaseModel):
    note_id: uuid.UUID
    note_title: str
    note_content: str
    created_on: datetime
    last_update:datetime

class NoteUpdate(BaseModel):
    note_title: Optional[str] = None
    note_content: Optional[str] = None


    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda v: v.isoformat()} 
