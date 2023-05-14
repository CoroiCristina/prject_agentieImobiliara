from fastapi import APIRouter
from .complexe import complexe_router
from .apartments import apartments_router
from .extra_options import extra_options_router

api_endpoints = APIRouter()
api_endpoints.include_router(complexe_router)
api_endpoints.include_router(apartments_router)
api_endpoints.include_router(extra_options_router)
