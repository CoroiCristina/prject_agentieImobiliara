from fastapi import APIRouter
from config import get_storage
from model.modelComplex import Complex

complexe_router = APIRouter(prefix="/complexe", tags=["complexe"])
store = get_storage()


@complexe_router.get("/", tags=['complexe'])
def get_complexe():
    return store.get_complexe()


@complexe_router.get("/{id_complex}", tags=['complexe'])
def get_complex_by_id(id_complex):
    #if len(store.get_complex_by_id())> 0:
    return store.get_complex_by_id(id_complex)
    #return HTTPException(status_code=404, detail="Item not found")


@complexe_router.put("/", tags=['complexe'])
def put_complex(complex: Complex):
    res = store.put_complex(complex)
    return res
