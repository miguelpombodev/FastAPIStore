from fastapi import APIRouter

from ..modules.products.services.list_products_service import ListProductsService

router = APIRouter(prefix="/products")


@router.get("")
async def get_products():
    listProductsService = ListProductsService()

    products = listProductsService.execute()

    return products
