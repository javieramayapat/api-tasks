from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..models.models import Task
from ..schemas import task_schema


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task_detail(db: Session, id: int):
    return db.query(Task).filter(Task.id == id).first()


def create_task(db: Session, task: task_schema.TaskCreate):
    db_task = Task(user_id=task.user_id,
                   title=task.title,
                   description=task.description,
                   due_date=task.due_date,
                   status=task.status)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def update_task(db: Session, id:int, task_update: task_schema.TaskUpdate):
    task = db.query(Task).filter(Task.id == id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = task_update.title
    task.description = task_update.description
    task.due_date = task_update.due_date
    task.status = task_update.status

    db.add(task)
    db.commit()

    return task


def delete_task(db: Session, id: int):
    task = db.query(Task).filter(Task.id == id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return status.HTTP_204_NO_CONTENT
