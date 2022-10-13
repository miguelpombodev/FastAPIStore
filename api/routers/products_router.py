from api.modules.products.model import Product
from api.modules.products.services.list_products_service import ListProductsService

from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.get("")
async def get_products():
    listProductsService = ListProductsService()

    products = listProductsService.execute()

    return products
