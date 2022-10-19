from api.modules.products.model import Product
from api.modules.products.services import ListProductsService, GetProductByIDService

from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.get("", response_model=list[Product])
async def get_products():
    listProductsService = ListProductsService()

    products = listProductsService.execute()

    return products


@router.get("/{product_id}")
async def get_product_by_id(product_id: str):
    getProductByIDService = GetProductByIDService()

    product = getProductByIDService.execute(product_id)

    return product
