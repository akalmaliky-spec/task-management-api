"""Task CRUD. Users can only see and change their own tasks."""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Task, User
from app.schemas import TaskCreate, TaskOut, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _get_own_task(db: Session, task_id: int, user: User) -> Task:
    task = db.get(Task, task_id)
    if task is None or task.owner_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.get("/", response_model=list[TaskOut])
def list_tasks(
    completed: bool | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[Task]:
    stmt = select(Task).where(Task.owner_id == current_user.id)
    if completed is not None:
        stmt = stmt.where(Task.completed == completed)
    stmt = stmt.order_by(Task.id).offset(skip).limit(limit)
    return list(db.scalars(stmt))


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Task:
    task = Task(**task_in.model_dump(), owner_id=current_user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> Task:
    return _get_own_task(db, task_id, current_user)


@router.patch("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Task:
    task = _get_own_task(db, task_id, current_user)
    for field, value in task_in.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> None:
    task = _get_own_task(db, task_id, current_user)
    db.delete(task)
    db.commit()
