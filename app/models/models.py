from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship

from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(50), nullable=False)

    trips = relationship("Task")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(String(250), nullable=False)
    due_date = Column(Date)
    status = Column(Enum("pending", "in progress", "completed", "required"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)