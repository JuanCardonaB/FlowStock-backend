from fastapi import APIRouter
from models.response_model import APIResponse
from products.infrastructure.products_infrastructure import get_products
from users_types.infrastructure.users_types_infrastructure import get_users_types

# This is the router for the users types.
router = APIRouter()

# This route returns all users types.
@router.get("", response_model=APIResponse)
def all_users_types():
    return get_users_types()