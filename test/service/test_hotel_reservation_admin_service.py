from unittest import TestCase

from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room
from hotelReservation.data.model.Room_Type import RoomType
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.services.customer_service_implementation import CustomerReservationImplementation
from hotelReservation.services.hotel_reservation_admin_service import HotelReservationAdminService
from hotelReservation.services.reservation_service_implementation import ReservationServicesImplementation
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


def build_customer():
    request = RegistrationRequest()
    request.set_first_name("Ola")
    request.set_last_name("Ola")
    request.set_email("Oladi@gmail.com")
    return request


def build_booking_request():
    booking_request = BookRoomRequest()
    customer = Customer()
    customer.set_email("Oladi@gmail.com")
    customer.set_first_name("Ola")
    customer.set_last_name("Ola")
    booking_request.set_customer(customer)

    booking_request.set_room_type("single")
    booking_request.set_check_in_date("2033-07-29")
    booking_request.set_check_out_date("2033-07-30")

    return booking_request


class TestHotelReservationAdminService(TestCase):
    admin_services = HotelReservationAdminService()
    customer_services = CustomerReservationImplementation()
    reservation_services = ReservationServicesImplementation()
    room_serv = RoomServiceImplementation()
    reservations = build_booking_request()

    def test_get_all_customers(self):
        customer = build_customer()
        saved_customer = self.customer_services.register(customer)
        self.assertIsNotNone(saved_customer)
        self.assertEqual(Customer, self.admin_services.get_all_customers().__class__)

    def test_display_all_reservations(self):
        customer = build_customer()
        new_room = Room()
        new_room.set_room_type(RoomType.SINGLE)
        new_room.set_room_price(4500)
        saved_room = self.room_serv.save_room(new_room)
        self.assertIsNotNone(saved_room)

        saved_customer = self.customer_services.register(customer)
        self.assertIsNotNone(saved_customer)

        booking_request = BookRoomRequest()
        customer = Customer()
        customer.set_email("Oladi@gmail.com")
        customer.set_first_name("Ola")
        customer.set_last_name("Ola")
        booking_request.set_customer(customer)

        booking_request.set_room_type(RoomType.SINGLE)
        booking_request.set_check_in_date("2033-07-29")
        booking_request.set_check_out_date("2033-07-30")

        reserved_room = self.reservation_services.book_room(booking_request)
        self.assertIsNotNone(reserved_room)
        self.assertEqual(1, len(self.admin_services.display_all_reservations()))

    def test_get_customer(self):
        customer = build_customer()
        saved_customer = self.customer_services.register(customer)
        self.assertIsNotNone(saved_customer)
        found_customer = self.admin_services.get_customer(saved_customer.get_email())
        self.assertIsNotNone(found_customer)

    def test_add_room(self):
        room = Room()
        room.set_room_type(RoomType.DOUBLE)
        room.set_room_price(10000)

        saved_room = self.admin_services.add_room(room)
        self.assertIsNotNone(saved_room)

    def test_get_all_rooms(self):
        room = Room()
        room.set_room_type(RoomType.DOUBLE)
        room.set_room_price(10000)

        saved_room = self.admin_services.add_room(room)
        self.assertIsNotNone(saved_room)

        room1 = Room()
        room.set_room_type(RoomType.SINGLE)
        room.set_room_price(5000)
        saved_room1 = self.admin_services.add_room(room1)
        self.assertIsNotNone(saved_room1)
        number_of_room = self.admin_services.get_all_rooms()

        self.assertEqual(len(number_of_room), len(self.admin_services.get_all_rooms()))

    def test_save_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_serv.save_room(new_room)
        self.assertIsNotNone(saved_room)
        print(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("DOUBLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_serv.save_room(new_room1)
        self.assertIsNotNone(saved_room1)
        print(saved_room1)

        new_room2 = Room()
        new_room2.set_room_type("SINGLE")
        new_room2.set_room_price(4500)
        saved_room2 = self.room_serv.save_room(new_room2)
        self.assertIsNotNone(saved_room2)
        print(saved_room2)
