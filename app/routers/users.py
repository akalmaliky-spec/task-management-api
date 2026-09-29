"""Current-user profile endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import User
from app.schemas import UserOut, UserUpdate
from app.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.patch("/me", response_model=UserOut)
def update_me(
    user_in: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> User:
    data = user_in.model_dump(exclude_unset=True)
    if "full_name" in data:
        current_user.full_name = data["full_name"]
    if data.get("password"):
        current_user.hashed_password = hash_password(data["password"])
    db.commit()
    db.refresh(current_user)
    return current_user
