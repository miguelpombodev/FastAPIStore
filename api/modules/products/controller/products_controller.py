from ..services import (
    ListProductsService,
    GetProductByIDService, 
    SaveProductService
)

from api.shared.errors import (
    ServiceError,
    ControllerError
)

from api.modules.products.model.validations import Product

class ProductsController:
    def get_one_product(self, id: str):
        try:
            _service = GetProductByIDService()

            product = _service.execute(id)

            return product
        except ServiceError as e:
            raise ControllerError(status_code=500,message=e)

    def get_products_list(self):
        try:
            _service = ListProductsService()

            products = _service.execute()

            return products
        except ServiceError as e:
            raise ControllerError(status_code=500,message=e)

    def save_product(self, product: Product):
        try:
            _service = SaveProductService()

            result = _service.execute(product)

            return result
        except ServiceError as e:
            raise ControllerError(status_code=500,message=e)