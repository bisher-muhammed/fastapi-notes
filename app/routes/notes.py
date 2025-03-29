from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import NoteCreate, NoteResponse,NoteUpdate
from app.crud import create_note, get_notes, update_note, delete_note
from app.auth import get_current_user  # Import JWT authentication
from typing import List
import uuid
from datetime import datetime
from app.models import Note


router = APIRouter()

@router.post("/create", response_model=NoteResponse)
def create_new_note(note: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Create a new note - Only authenticated users can do this. """
    return create_note(db, note, current_user.user_id)

@router.get("/", response_model=List[NoteResponse])
def get_all_notes(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Retrieve all notes for the authenticated user. """
    return get_notes(db, current_user.user_id)

@router.put("/{note_id}", response_model=NoteResponse)
def update_existing_note(note_id: uuid.UUID, note_data: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Update a note - Only if it belongs to the authenticated user. """
    note = update_note(db, note_id, note_data, current_user.user_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")
    return note



@router.patch("/notes/{note_id}", response_model=NoteUpdate)
def patch_update_note(note_id: str, note_data: NoteUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    note = db.query(Note).filter(Note.note_id == note_id, Note.user_id == current_user.user_id).first()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")
    
    if note_data.note_title is not None:
        note.note_title = note_data.note_title
    if note_data.note_content is not None:
        note.note_content = note_data.note_content
    
    note.last_update = datetime.utcnow()  # Update timestamp
    db.commit()
    db.refresh(note)
    
    return note



@router.delete("/{note_id}")
def delete_existing_note(note_id: uuid.UUID, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Delete a note - Only if it belongs to the authenticated user. """
    note = delete_note(db, note_id, current_user.user_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")
    return {"message": "Note deleted successfully"}
