# @router.get("/", response_model=List[UserOut])
# def list_users(db: Session = Depends(get_db)):
#     """
#     Возвращает список всех пользователей.
#     Может быть полезно для административных целей.
#     """
#     return db.query(User).all()
#
# @router.get("/{user_id}", response_model=UserOut)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     """
#     Возвращает пользователя по ID.
#     Выбрасывает ошибку, если пользователь не найден.
#     """
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from routers.utils import get_password_hash
from schemas.user import UserCreate, UserOut

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
