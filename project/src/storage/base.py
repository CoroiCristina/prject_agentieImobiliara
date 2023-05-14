from abc import ABC, abstractmethod
from typing import List


class StorageObject(ABC):

    @abstractmethod
    def get_complex_by_id(self, id_complex: int) -> List[object]:
        raise NotImplementedError("Functia get_complex_by_id neimplementata")

    @abstractmethod
    def get_complexe(self) -> List[object]:
        raise NotImplementedError("Functia get_complexe neimplementata")

    @abstractmethod
    def put_complex(self, complex: object) -> List[object]:
        raise NotImplementedError("Functia put_complex neimplementata")

    @abstractmethod
    def get_all_apartments(self) -> List[object]:
        raise NotImplementedError("Functia get_all_apartments neimplementata")

    @abstractmethod
    def get_apartments_by_strada(self, strada: str) -> List[object]:
        raise NotImplementedError("Functia get_apartments_by_strada neimplementata")

    @abstractmethod
    def get_apartment_by_id(self, id_ap: int) -> List[object]:
        raise NotImplementedError("Functia get_apartment_by_id neimplementata")

    @abstractmethod
    def update_apartment_statut(self, status: str, apartament: object) -> List[object]:
        raise NotImplementedError("Functia update_apartament_statut neimplementata")

    @abstractmethod
    def get_all_extra_options(self) -> List[object]:
        raise NotImplementedError("Functia get_all_extra_options neimplementata")

    @abstractmethod
    def get_extra_option_by_id(self, id_op: int) -> List[object]:
        raise NotImplementedError("Functia get_extra_option_by_id neimplementata")

    @abstractmethod
    def put_extra_option(self, extra_optiune: object) -> List[object]:
        raise NotImplementedError("Functia put_extra_option neimplementata")

    @abstractmethod
    def delete_extra_option(self, id_op: int) -> List[object]:
        raise NotImplementedError("Functia delete_extra_option neimplementata")

    # @abstractmethod
    # def get_all_clients(self) -> List[object]:
    #     raise NotImplementedError("Functia get_all_clients neimplementata")

    # @abstractmethod
    # def get_client_by_cnp(self, CNP: str) -> List[object]:
    #     raise NotImplementedError("Functia get_client_by_cnp neimplementata")

    # @abstractmethod
    # def put_client(self, client: object) -> List[object]:
    #     raise NotImplementedError("Functia put_client neimplementata")

    # @abstractmethod
    # def get_all_contracts(self) -> List[object]:
    #     raise NotImplementedError("Functia get_all_contracts neimplementata")

    # def get_contract_by_id_ap(self) -> List[object]:
    #     raise NotImplementedError("Functia get_contract_by_id_apartament neimplementata")

    # def put_contract(self, contract: object) -> List[object]:
    #     raise NotImplementedError("Functia put_contract neimplementata")

    # @abstractmethod
    # def get_all_sales(self) -> List[object]:
    #     raise NotImplementedError("Functia get_all_sales neimplementata")

    # @abstractmethod
    # def get_sale_by_nr_contract(self, nr_contract: str) -> List[object]:
    #     raise NotImplementedError("Functia get_sale_by_nr_contract neimplementata")

    # @abstractmethod
    # def get_all_rentals(self) -> List[object]:
    #     raise NotImplementedError("Functia get_all_rentals neimplementata")

    # @abstractmethod
    # def get_rental_by_nr_contract(self, nr_contract: str) -> List[object]:
    #     raise NotImplementedError("Functia get_rental_by_nr_contract neimplementata")

    # @abstractmethod
    # def get_inregistrari_cont_bancar(self) -> List[object]:
    #     raise NotImplementedError("Functia get_inregistrari_cont_bancar neimplementata")

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
