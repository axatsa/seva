from fastapi import FastAPI
from fastapi import APIRouter, UploadFile, File
from products import AddToysValidator,EditToysValidator,DeleteToysValidator
from typing import List

from database.product_service import (add_art_pr_db,edit_art_pr_db,delete_art_pr_db,get_all_art_pr_db,get_exact_art_pr_db)

product_router = APIRouter(prefix='/toy', tags=['Управление игрушками'])

