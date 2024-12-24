from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    product_ids: List[int]
    total_amount: float

class OrderOut(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str

    class Config:
        orm_mode = True
