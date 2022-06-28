from fastapi import APIRouter
# from ..modules.products.services import GetProductService
from ..shared.providers.database.config import connection_string


router = APIRouter(prefix="/products")


@router.get("")
async def get_products():
    # products = await GetProductService.execute()
    print(connection_string)

    return {"message": 'asdada'}
