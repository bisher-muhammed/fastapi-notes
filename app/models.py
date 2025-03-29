from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import uuid
import datetime
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4())) 
    user_name = Column(String(255), nullable=False)
    user_email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)  # Fixed typo
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    last_update = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    notes = relationship("Note", back_populates="user", cascade="all, delete")  # Add this

class Note(Base):
    __tablename__ = "notes"

    note_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    note_title = Column(String(255), nullable=False)
    note_content = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    last_update = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user = relationship("User", back_populates="notes")  # Add this
