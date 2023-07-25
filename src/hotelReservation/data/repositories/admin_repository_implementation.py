from typing import Any

from hotelReservation.AppUtils.Utils import Utils
from hotelReservation.data.model.Admin import Admin
from hotelReservation.data.repositories.admin_repository import AdminRepository


class AdminRepositoryImplementation(AdminRepository):

    def __init__(self):
        self.admin_list: [Admin] = []

    def save_admin(self, admin: Admin) -> Admin:
        admin.set_admin_id(Utils.generate_id())
        self.admin_list.append(admin)
        return admin

    def find_admin_by_id(self, admin_id) -> Admin | None:
        for admin in self.admin_list:
            if admin.get_admin_id() == admin_id:
                return admin
        return None

    def delete_admin_by_id(self, admin_id):
        found_admin = self.find_admin_by_id(admin_id)
        if found_admin is not None:
            self.admin_list.remove(found_admin)


    def update_admin(self, admin: Admin) -> Admin:
        pass
