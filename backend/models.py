
from pydantic import BaseModel

# Give type for each field of product class
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

   