from fastapi import APIRouter
from ..modules.products.model import Product
# from ..shared.providers.database.config import connection_string


router = APIRouter(prefix="/products")


@router.get("")
async def get_products():

    products = Product.getProducts()

    return products
