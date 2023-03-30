from fastapi import APIRouter, Body, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..schemas import task_schema
from ..services import task_service


router = APIRouter(prefix="/tasks", tags=['Tasks'])


@router.get(path='/tasks', response_model=list[task_schema.TaskOut], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    tasks = task_service.get_tasks(db=db)
    return tasks


@router.get(path='/tasks/{id}', response_model=task_schema.TaskOut, status_code=status.HTTP_200_OK)
def get_tasks_detail(db: Session = Depends(get_db), id: int = Path(..., gt=0, example=1)):
    task = task_service.get_task_detail(db=db, id=id)
    return task


@router.post(path='/tasks', response_model=task_schema.TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task(db: Session = Depends(get_db), task: task_schema.TaskCreate = Body(...)):
    return task_service.create_task(db=db, task=task)


@router.put(path='/tasks/{id}', response_model=task_schema.TaskUpdate, status_code=status.HTTP_200_OK)
def update_task(db: Session = Depends(get_db), id: int = Path(..., gt=0, example=1), task: task_schema.TaskUpdate = Body(...)):
    return task_service.update_task(db=db, id=id, task_update=task)


@router.delete(path='/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(db: Session = Depends(get_db), id: int = Path(..., gt=0, example=1)):
    return task_service.delete_task(db=db, id=id)