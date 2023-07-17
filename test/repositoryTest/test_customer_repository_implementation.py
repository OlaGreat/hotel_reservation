from unittest import TestCase

from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.repositories.customer_repository_implementation import CustomerRepositoryImplementation


def build_customer():
    customer = Customer()
    customer.set_email("Ola@gmail")
    customer.set_first_name("Ola")
    customer.set_last_name("Oal")

    return customer


class TestCustomerRepositoryImplementation(TestCase):
    customer_repository = CustomerRepositoryImplementation()

    def test_save_customer(self):
        customer1 = build_customer()
        saved_customer = self.customer_repository.save_customer(customer1)
        self.assertIsNotNone(saved_customer)

    def test_find_customer_by_id(self):
        customer1 = build_customer()
        saved_customer = self.customer_repository.save_customer(customer1)
        self.assertIsNotNone(saved_customer)

        found_customer = self.customer_repository.find_customer_by_id(customer1.get_customer_id())
        self.assertIsNotNone(found_customer)

    def test_delete_customer_by_id(self):
        customer = build_customer()
        saved_customer = self.customer_repository.save_customer(customer)
        self.assertIsNotNone(saved_customer)
        self.customer_repository.delete_customer_by_id(customer.get_customer_id())

    def test_get_all_customer(self):
        customer = build_customer()
        saved_customer = self.customer_repository.save_customer(customer)
        self.assertIsNotNone(saved_customer)
        nuw = self.customer_repository.get_all_customer()
        self.assertEqual(len(nuw), len(self.customer_repository.get_all_customer()))

    def test_get_customer_by_email(self):
        customer = build_customer()
        saved_customer = self.customer_repository.save_customer(customer)
        self.assertIsNotNone(saved_customer)
        found_customer = self.customer_repository.find_by_email(customer.get_email())
        self.assertEqual(found_customer, customer)
