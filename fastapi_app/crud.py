from sqlalchemy.orm import Session

from . import models, schemas


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    fake_hashed_password = client.password + "notreallyhashed"
    db_client = models.Client(email=client.email, hashed_password=fake_hashed_password)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_checks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Check).offset(skip).limit(limit).all()


def create_client_check(db: Session, check: schemas.CheckCreate, client_id: int):
    db_check = models.Check(**check.dict(), owner_id=client_id)
    db.add(db_check)
    db.commit()
    db.refresh(db_check)
    return db_check
