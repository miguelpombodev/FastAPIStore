from ..repository.products_repository import ProductsRepository

from ..model.validations import FullDetailProduct

class GetDetailedProductByIDService:
    def __init__(self) -> None:
        self._repository = ProductsRepository()

    def execute(self, product_id: str) -> FullDetailProduct:

        orm_result = self._repository.get_detailed_by_id(product_id).__dict__

        normalized_orm = self.__set_to_response_model__(orm_result)

        product = FullDetailProduct(**normalized_orm)

        return product

    def __set_to_response_model__(self, orm_result: dict):
        product_brand, product_type, product_colors = FullDetailProduct.serialize_dict(
                                                                                                    brand=orm_result["product_brand"],
                                                                                                    colors_list=orm_result["product_colors"],
                                                                                                    type=orm_result["product_type"],
                                                                                                )
        orm_result["product_brand"] = product_brand
        orm_result["product_type"] = product_type
        orm_result["product_colors"] = product_colors   

        return orm_result                                                                                         
