from abc import ABC, abstractmethod

from hotelReservation.data.model.Admin import Admin


class AdminRepository(ABC):

    @abstractmethod
    def save_admin(self, admin: Admin) -> Admin:
        pass

    @abstractmethod
    def find_admin_by_id(self, admin_id) -> Admin:
        pass

    @abstractmethod
    def delete_admin_by_id(self, admin_id):
        pass

    @abstractmethod
    def update_admin(self, admin: Admin) -> Admin:
        pass
