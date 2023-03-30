from fastapi import APIRouter, Body, HTTPException, status, Path, Depends


from ..schemas import task_schema


router = APIRouter(prefix="/tasks", tags=['Tasks'])


@router.get(path='/tasks', response_model=list[task_schema.TaskOut], status_code=status.HTTP_200_OK)
def get_tasks():
    pass


@router.get(path='/tasks/{id}', response_model=task_schema.TaskOut, status_code=status.HTTP_200_OK)
def get_tasks_detail(id: int = Path(..., gt=0, example=1)):
    pass


@router.post(path='/tasks', response_model=task_schema.TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task( task: task_schema.TaskCreate = Body(...)):
    pass


@router.put(path='/tasks/{id}', response_model=task_schema.TaskUpdate, status_code=status.HTTP_200_OK)
def update_task(id: int = Path(..., gt=0, example=1)):
    pass


@router.delete(path='/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int = Path(..., gt=0, example=1)):
    pass