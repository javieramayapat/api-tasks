from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base schema is  a class that allows me abstract the orm_mode from schemas and  provide them base on inherit
    """
    class Config:
        orm_mode = True