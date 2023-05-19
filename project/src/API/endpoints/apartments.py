from fastapi import APIRouter
from config import get_storage
from model.modelApartament import Apartament

apartments_router = APIRouter(prefix="/apartments", tags=["aparatmens"])
store = get_storage()


@apartments_router.get("/", tags=['apartments'])
def get_all_apartments():
    return store.get_all_apartments()


@apartments_router.get("/strada/{strada}", tags=['apartments'])
def get_apartment_by_strada(strada):
    return store.get_apartments_by_strada(strada)


@apartments_router.get("/{id_ap}", tags=['apartments'])
def get_apartment_by_id(id_ap):
    return store.get_apartment_by_id(id_ap)


@apartments_router.post("/{status}/{id_ap}", tags=['apartments'])
def update_apartment_statut(status: str, id_ap: int):
    return update_apartment_statut(status, id_ap)
