from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials
from auth import security, authenticate_user, is_admin
from models import Product
from utils import load_data, save_data, hash_password

app = FastAPI()

products_filename = "products.json"
cart_filename = "cart.json"
users_filename = "users.json"

@app.post("/admin/add_product/")
def add_product(name: str, price: float, credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate_user(credentials, users_filename)
    if not is_admin(user):
        raise HTTPException(status_code=403, detail="Forbidden")
    products = load_data(products_filename)
    products.append(Product(name, price).to_dict())
    save_data(products, products_filename)
    return {"message": "Product added successfully"}

@app.get("/products/")
def get_products():
    return load_data(products_filename)

@app.post("/cart/add/")
def add_to_cart(product_name: str, credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate_user(credentials, users_filename)
    products = load_data(products_filename)
    product = next((p for p in products if p["name"] == product_name), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    cart = load_data(cart_filename)
    if credentials.username not in cart:
        cart[credentials.username] = []
    cart[credentials.username].append(product)
    save_data(cart, cart_filename)
    return {"message": "Product added to cart successfully"}
