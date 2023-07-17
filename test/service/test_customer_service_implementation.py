from unittest import TestCase

from hotelReservation.data.model.Room import Room
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest
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
        self.assertEqual(1, len(self.customer_services.get_all_customer()))

    def test_search_for_room(self):
        self.test_build_room()
        customer_to_register = build_customer()
        registered_customer = self.customer_services.register(customer_to_register)
        self.assertIsNotNone(registered_customer)

        book_room_request = RoomSearchRequest()
        book_room_request.set_room_type("SINGLE")
        book_room_request.set_check_out_date("2023-07-20")
        book_room_request.set_checkin_date("2023-07-15")
        found_room = self.customer_services.search_for_room(book_room_request)
        self.assertIsNotNone(found_room)
        print(found_room)

    def test_book_room(self):
        pass

    def test_view_reservation(self):
        pass

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
