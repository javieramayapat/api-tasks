from datetime import date
from typing import Optional
from enum import Enum
from pydantic import Field
from .base_schema import BaseSchema


class TaskStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in progress'
    completed = 'completed'
    required = 'required'

class TaskBase(BaseSchema):
    title: str = Field(max_length=150, example="Create my first task")
    description: str = Field(max_length=250, example="Tasks for finish the project")
    due_date: Optional[date] = Field(default=None)
    status: TaskStatus = Field(example="in progress")


class TaskCreate(TaskBase):
    user_id: int = Field(gt=0, example=1)


class TaskUpdate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int = Field(gt=0, example=1)