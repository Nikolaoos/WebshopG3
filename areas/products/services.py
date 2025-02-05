from sqlalchemy import false
from models import Category, Newsletter, Product

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(1,4,False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts():
    return Product.query.order_by(Product.ProductID.desc()).paginate(1,8,False).items

def checkIfNewsletterSubscribed(email:str)-> bool:
    subscribed = Newsletter.query.filter(Newsletter.email == email).first()
    return True if subscribed else False