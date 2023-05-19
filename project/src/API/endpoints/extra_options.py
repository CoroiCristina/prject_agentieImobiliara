from fastapi import APIRouter
from config import get_storage
from model.modelExtraOptiune import ExtraOp

extra_options_router = APIRouter(prefix="/extra_options", tags=["extra_options"])
store = get_storage()


@extra_options_router.get("/", tags=['extra_options'])
def get_all_extra_options():
    return store.get_all_extra_options()


@extra_options_router.get("/{id_op}", tags=['extra_options'])
def get_extra_option_by_id(id_op):
    return store.get_extra_option_by_id(id_op)

@extra_options_router.put("/", tags=['extra_options'])
def put_extra_option(extra_optiune: ExtraOp):
    return store.put_extra_option(extra_optiune)

@extra_options_router.delete("/{id_op}", tags=['extra_options'])
def delete_extra_option(id_op):
    return store.delete_extra_option(id_op)