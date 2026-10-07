from fastapi import FastAPI
from models import Product

app = FastAPI()

# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/")
def greet():
    return "Hello world"


@app.get("/products")
def get_all_products():
    return products;


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if (product.id == product_id):
            return product;
    return {"error": "No product found"}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == product_id:
            products[i] = product
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}