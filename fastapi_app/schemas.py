from typing import List

from pydantic import BaseModel


class CheckBase(BaseModel):
    title: str
    description: str = None


class CheckCreate(CheckBase):
    pass


class Check(CheckBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    email: str


class ClientCreate(ClientBase):
    password: str


class Client(ClientBase):
    id: int
    is_active: bool
    checks: List[Check] = []

    class Config:
        orm_mode = True
