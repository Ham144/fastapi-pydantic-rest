
from fastapi import APIRouter, status
from pydantic import BaseModel


router = APIRouter(
    prefix="/api/products",
    tags=['Product']
)

class Product(BaseModel):
    sku: str
    desc: str | None = None
    qty_mangga_dua: int = 0
    qty_pluit: int = 0

class Product_edit(BaseModel):
    desc: str | None
    qty_mangga_dua: int 
    qty_pluit: int 

inventories : list[Product] = [
    Product(
        sku=120,
        desc="this is a 120 product",
        qty_mangga_dua=23,
        qty_pluit=25
    ),
    Product(
        sku=160,
        desc="this is a 160 product",
        qty_mangga_dua=55,
        qty_pluit=14
    )
]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_product(body: Product):
    

