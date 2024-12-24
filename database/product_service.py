from .models import Product
from . import get_db


# добовление товара
def add_art_pr_db(name, description, price, stock, category):
    with next(get_db()) as db:
        new_art_pr = Product(name=name, description=description,
                          price=price,stock=stock,category=category)
        db.add(new_art_pr)
        db.commit()
        return {'message': f'Товар успешно добавлен {new_art_pr.name}'}


# получени всех товаров
def get_all_art_pr_db():
    pass


# получение определенного товара
def get_exact_art_pr_db():
    pass


# Удалеине товара
def delete_art_pr_db():
    pass


# Изменение товара
def edit_art_pr_db():
    pass
