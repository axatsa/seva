from .models import User
from . import get_db
from datetime import datetime


# Регистрация пользователя
def add_user_db(name, email, hashed_password, role):
    db = get_db()

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return True

    new_user = User(name=name, email=email, hashed_password=hashed_password,role=role, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return f'Пользователь усепешно добавлен'


# Получение всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


# Получение определенного пользователя
def get_exact_user_db(id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=id).first()

    return exact_user


# Удаление пользователя
def delete_user_db(id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(id=id).first()

    db.delete(delete_user)
    db.commit()
    return f'Пользователь с {id} успешно удален'


# Изменение данные пользователя
def edit_user_db(id, name, email, hashed_password):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=id).first()

    if exact_user:
        if email is not None:
            exact_user.email = email

        if name is not None:
            exact_user.name = name

        if hashed_password is not None:
            exact_user.hashed_password = hashed_password

        db.commit()
        return {'message': 'Информация о пользователе успешно изменена'}
    else:
        return {'message': 'Не удалось найти пользователя с указанным идентификатором'}
