from pydantic import Field, EmailStr

from .base_schema import BaseSchema


class UserBase(BaseSchema):
    name: str = Field(max_length=50, example="Javier")
    last_name: str = Field(max_length=50, example="Amaya")
    username: str = Field(max_length=50, example="javieramayapat")
    email: EmailStr = Field(example="javieramayapat@gmail.com")


class UserIn(UserBase):
    password: str = Field(max_length=50)
