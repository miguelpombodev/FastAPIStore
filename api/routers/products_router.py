
from fastapi import APIRouter, HTTPException

from api.shared.errors.controller_error import ControllerError
from api.modules.products.model.validations import FullDetailProduct, Product
from api.modules.products.controller.products_controller import ProductsController

router = APIRouter(prefix="/products", tags=["Products"])

_controller = ProductsController()

@router.get("", description="This endpoint returns all products saved in database")
def get_products():
    try:
        products_list = _controller.get_products_list()

        return products_list
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.get("/{product_id}", description="This endpoint return all details of a product")
def get_product_by_id(product_id: str):
    try:
        product = _controller.get_detailed_one_product(product_id)
        return product
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

@router.post("/create", description="This endpoint saves a product in database")
def save_product(product: Product):
    try:
        result = _controller.save_product(product)

        return {
                "message": "Product saved",
                "status": result
            }
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code,detail={
                "status": False,            
                "message": str(e.message)
        })

@router.put("/update/{product_id}", description="This endpoint updates a product saved in database")
def update_product(
    product_id: str,
    product: Product
):
    try:
        result = _controller.update_one(product_id, product)

        return result
    except ControllerError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)