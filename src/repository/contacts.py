from typing import List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate
from sqlalchemy.sql import extract
from sqlalchemy import func, and_


async def find_contacts(contacts_find_data : str, db: Session) -> Contact | None :
    result =  db.query(Contact).filter(Contact.first_name == contacts_find_data).all()
    if result:
        return result
    result =  db.query(Contact).filter(Contact.second_name == contacts_find_data).all()
    if result:
        return result
    result =  db.query(Contact).filter(Contact.mail == contacts_find_data).all()
    if result:
        return result

#---------------
def find_contacts_by_birthday_month_and_day(db: Session, month: int, day: int) ->list:
    contacts = db.query(Contact).filter(
        extract('month', Contact.birthday) == month,
        extract('day', Contact.birthday) == day
    ).all()
    return contacts

async def find_contacts_delta_time(contact_find_days : int, db: Session) ->  List[Contact]:
    current_date = datetime.now().date()
    dates= []
    result = []
    for i in range(contact_find_days):
        dates.append(current_date+timedelta(days=i))
    for d in dates:
        result.extend( find_contacts_by_birthday_month_and_day(db, month = d.month, day = d.day )  )
    return  result
#--------------------


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()
        

async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, second_name=body.second_name, mail=body.mail, birthday=body.birthday, addition=body.addition)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.second_name = body.second_name
        contact.mail = body.mail
        contact.birthday = body.birthday
        contact.addition = body.addition
        db.commit()
    return contact

