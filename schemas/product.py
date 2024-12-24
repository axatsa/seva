from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category: str

    class Config:
        orm_mode = True
