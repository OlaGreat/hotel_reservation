from unittest import TestCase

from hotelReservation.data.model.Admin import Admin
from hotelReservation.data.repositories.admin_repository_implementation import AdminRepositoryImplementation


def build_admin():
    admin = Admin()
    admin.set_first_name("Tola")
    admin.set_last_name("Bolu")
    admin.set_email("Bola@gmail")
    return admin


class TestAdminRepositoryImplementation(TestCase):
    admin_repo = AdminRepositoryImplementation()

    def test_save_admin(self):
        admin = build_admin()
        saved_admin = self.admin_repo.save_admin(admin)
        self.assertIsNotNone(saved_admin)

    def test_find_admin_by_id(self):
        admin = build_admin()
        saved_admin = self.admin_repo.save_admin(admin)
        self.assertIsNotNone(saved_admin)

        found_admin = self.admin_repo.find_admin_by_id(saved_admin.get_admin_id())
        self.assertIsNotNone(found_admin)

    def test_delete_admin_by_id(self):
        admin = build_admin()
        saved_admin = self.admin_repo.save_admin(admin)
        self.assertIsNotNone(saved_admin)

        self.admin_repo.delete_admin_by_id(saved_admin.get_admin_id())
        self.assertEqual(0, len(self.admin_repo.admin_list))

    def test_update_admin(self):
        admin = build_admin()
        saved_admin = self.admin_repo.save_admin(admin)
        self.assertIsNotNone(saved_admin)





