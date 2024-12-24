from pydantic import BaseModel


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    name: str
    email: str
    hashed_password: str
    role: str


class DeleteUserValidator(BaseModel):
    id: int


# Валидатор для изменения пользователя
class EditUserValidator(BaseModel):
    id: int
    phone_number: str
    email: str
    password: str

