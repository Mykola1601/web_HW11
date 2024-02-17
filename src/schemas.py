from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, PastDate


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50, min_length=3)
    second_name: str = Field(max_length=50, min_length=3)
    mail: EmailStr = Field(max_length=60, min_length=6)
    birthday: PastDate
    addition: str = Field(max_length=300)

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name}"


class ContactResponse(ContactModel):
    id: int
    first_name: str  
    second_name: str 
    mail: EmailStr  
    birthday: PastDate 
    addition: str 
    created_at: datetime

    class Config:
        orm_mode = True


class ContactUpdate(ContactModel):
    first_name: str  
    second_name: str 
    mail: EmailStr  
    birthday: PastDate 
    addition: str 
    created_at: datetime

    

class TagModel(BaseModel):
    name: str = Field(max_length=25)


class TagResponse(TagModel):
    id: int

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150)


class NoteModel(NoteBase):
    tags: List[int]


class NoteUpdate(NoteModel):
    done: bool


class NoteStatusUpdate(BaseModel):
    done: bool


class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    tags: List[TagResponse]

    class Config:
        orm_mode = True
