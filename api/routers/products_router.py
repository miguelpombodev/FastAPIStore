# from api.modules.products.model import Product
from fastapi import APIRouter, Body, HTTPException

from api.shared.errors.controller_error import ControllerError
from api.modules.products.model.validations import FullDetailProduct, Product
from api.modules.products.controller.products_controller import ProductsController

router = APIRouter(prefix="/products")

_controller = ProductsController()

@router.get("", response_model=list[Product])
def get_products():
    try:
        products_list = _controller.get_products_list()

        return products_list
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.get("/{product_id}", response_model=FullDetailProduct)
def get_product_by_id(product_id: str):
    try:
        product = _controller.get_one_product(product_id)
        return product
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

# @router.post("/create")
# def save_product(product: Product = Body):
#     try:
#         _save_product_service = SaveProductService()

#         result = _save_product_service.execute(product)

#         return {"message": result}
#     except Exception as e:
#         raise Exception(e)
