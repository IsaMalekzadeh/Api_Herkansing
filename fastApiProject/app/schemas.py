from pydantic import BaseModel
from typing import List



class TeamBase(BaseModel):
    name: str
    city: str

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
