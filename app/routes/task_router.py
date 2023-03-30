from fastapi import APIRouter, Body, HTTPException, status, Path, Depends


router = APIRouter(prefix="/tasks", tags=['Tasks'])


@router.get(path='/tasks', status_code=status.HTTP_200_OK)
def get_tasks():
    pass

@router.get(path='/tasks/{id}', status_code=status.HTTP_200_OK)
def get_tasks_detail():
    pass

@router.post(path='/tasks', status_code=status.HTTP_201_CREATED)
def create_task():
    pass


@router.put(path='/tasks/{id}', status_code=status.HTTP_200_OK)
def update_task():
    pass


@router.delete(path='/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task():
    pass