from time import sleep

from api.modules.products.model import Product
from api.modules.products.services import ListProductsService, GetProductByIDService, SaveProductService

from fastapi import APIRouter, Body

router = APIRouter(prefix="/products")


@router.get("")
def get_products():
    listProductsService = ListProductsService()

    products = listProductsService.execute()

    return products


@router.get("/{product_id}")
def get_product_by_id(product_id: str):
    getProductByIDService = GetProductByIDService()

    product = getProductByIDService.execute(product_id)

    return product

# @router.post("/create")
# def save_product(product: Product = Body):
#     try:
#         _save_product_service = SaveProductService()

#         result = _save_product_service.execute(product)

#         return {"message": result}
#     except Exception as e:
#         raise Exception(e)
