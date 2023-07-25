from unittest import TestCase

from hotelReservation.data.model.Room import Room
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.services.customer_service_implementation import CustomerReservationImplementation
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


def build_customer():
    request = RegistrationRequest()
    request.set_first_name("Ola")
    request.set_last_name("Ola")
    request.set_email("Oladi@gamail.com")
    return request


class TestCustomerReservationImplementation(TestCase):
    customer_services = CustomerReservationImplementation()
    room_serv = RoomServiceImplementation()

    def test_register(self):
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)


    def test_book_room(self):
        self.test_build_room()
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)

        book_room_request = BookRoomRequest()
        customer = build_customer()
        book_room_request.set_customer(customer)
        book_room_request.set_room_type("SINGLE")
        book_room_request.set_check_out_date("2025-08-01")
        book_room_request.set_check_in_date("2025-07-27")
        found_room = self.customer_services.book_room(book_room_request)
        self.assertIsNotNone(found_room)
        print(f"first booking {found_room}")

        book_room_request2 = BookRoomRequest()
        customer2 = build_customer()
        book_room_request2.set_customer(customer2)
        book_room_request2.set_room_type("SINGLE")
        book_room_request2.set_check_out_date("2025-07-27")
        book_room_request2.set_check_in_date("2025-07-19")
        found_room2 = self.customer_services.book_room(book_room_request2)
        self.assertIsNotNone(found_room2)
        print(f"second booking {found_room2}")

    def test_view_reservation(self):
        self.test_build_room()
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)

        book_room_request = BookRoomRequest()
        customer = build_customer()
        book_room_request.set_customer(customer)
        book_room_request.set_room_type("SINGLE")
        book_room_request.set_check_out_date("2053-08-01")
        book_room_request.set_check_in_date("2053-07-27")
        found_room = self.customer_services.book_room(book_room_request)
        self.assertIsNotNone(found_room)
        customer1_reservations = self.customer_services.view_customer_reservation(customer.get_email())
        print(customer1_reservations)

        book_room_request2 = BookRoomRequest()
        customer2 = build_customer()
        book_room_request2.set_customer(customer2)
        book_room_request2.set_room_type("SINGLE")
        book_room_request2.set_check_out_date("2053-07-27")
        book_room_request2.set_check_in_date("2053-07-19")
        found_room2 = self.customer_services.book_room(book_room_request2)
        self.assertIsNotNone(found_room2)
        customer2_reservations = self.customer_services.view_customer_reservation(customer2.get_email())
        print(customer2_reservations)

    def test_find_by_id(self):
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)
        found_customer = self.customer_services.find_customer_by_id(registered_customer.get_customer_id())
        self.assertEqual(found_customer, registered_customer)

    def test_delete_by_id(self):
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)
        self.customer_services.delete_customer_by_id(registered_customer.get_customer_id())
        self.assertEqual('there is no registered customer', self.customer_services.get_all_customer())

    def test_get_all_customer(self):
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)
        customer2 = build_customer()
        saved_room = self.customer_services.register(customer2)
        self.assertIsNotNone(saved_room)
        self.customer_services.get_all_customer()

    def test_build_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_serv.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("DOUBLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_serv.save_room(new_room1)
        self.assertIsNotNone(saved_room1)

        new_room2 = Room()
        new_room2.set_room_type("SINGLE")
        new_room2.set_room_price(4500)
        saved_room2 = self.room_serv.save_room(new_room2)
        self.assertIsNotNone(saved_room2)
