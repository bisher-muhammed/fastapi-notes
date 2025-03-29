from sqlalchemy.orm import Session
from app.models import Note
from app.schemas import NoteCreate
import uuid
from datetime import datetime


def create_note(db: Session, note: NoteCreate, user_id: int):
    """ Create a new note for the authenticated user. """
    db_note = Note(
        note_title=note.note_title,
        note_content=note.note_content,
        user_id=user_id  # Ensure note belongs to user
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session, user_id: int):
    """ Retrieve all notes for the authenticated user. """
    return db.query(Note).filter(Note.user_id == user_id).all()

def update_note(db: Session, note_id: uuid.UUID, note_data: NoteCreate, user_id: int):
    """ Update a note if it belongs to the authenticated user (supports partial updates). """
    note = db.query(Note).filter(Note.note_id == note_id, Note.user_id == user_id).first()
    if not note:
        return None  # Note not found or unauthorized

    # Apply updates only if provided
    if note_data.note_title is not None:
        note.note_title = note_data.note_title
    if note_data.note_content is not None:
        note.note_content = note_data.note_content

    note.last_update = datetime.utcnow()
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: uuid.UUID, user_id: int):
    """ Delete a note if it belongs to the authenticated user. """
    note = db.query(Note).filter(Note.note_id == note_id, Note.user_id == user_id).first()
    if note:
        db.delete(note)
        db.commit()
    return note
