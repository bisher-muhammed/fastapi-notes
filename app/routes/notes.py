from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import NoteCreate, NoteResponse, NoteUpdate
from app.crud import create_note, get_notes, update_note, delete_note
from app.auth import get_current_user  # Import JWT authentication
from typing import List
import uuid
from datetime import datetime
from app.models import Note

router = APIRouter()

@router.post("/create", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_new_note(
    note: NoteCreate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """ Create a new note - Only authenticated users can do this. """
    note_data = create_note(db, note, current_user.user_id)
    
    # Check if note creation was successful
    if not note_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Failed to create note"
        )
    
    # Return the created note data
    return note_data



@router.get("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def get_single_note(note_id: uuid.UUID, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    note = db.query(Note).filter(Note.note_id == note_id, Note.user_id == current_user.user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="No notes found")
    

    
    return note

@router.get("/", response_model=List[NoteResponse], status_code=status.HTTP_200_OK)
def get_all_notes(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Retrieve all notes for the authenticated user. """
    notes = get_notes(db, current_user.user_id)
    return notes

@router.put("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def update_existing_note(note_id: uuid.UUID, note_data: NoteCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Update a note - Only if it belongs to the authenticated user. """
    note = update_note(db, note_id, note_data, current_user.user_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found or unauthorized")
    return note

@router.patch("/notes/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def patch_update_note(note_id: str, note_data: NoteUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    note = db.query(Note).filter(Note.note_id == note_id, Note.user_id == current_user.user_id).first()
    
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found or unauthorized")
    
    if note_data.note_title is not None:
        note.note_title = note_data.note_title
    if note_data.note_content is not None:
        note.note_content = note_data.note_content
    
    note.last_update = datetime.utcnow()  # Update timestamp
    db.commit()
    db.refresh(note)
    
    return note

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_note(note_id: uuid.UUID, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """ Delete a note - Only if it belongs to the authenticated user. """
    note = delete_note(db, note_id, current_user.user_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found or unauthorized")
    return {"message": "Note deleted successfully"}


