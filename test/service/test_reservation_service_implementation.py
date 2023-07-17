from unittest import TestCase

from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.services.reservation_service_implementation import ReservationServicesImplementation
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


def build_booking_request():
    booking_request = BookRoomRequest()
    customer = Customer()
    customer.set_email("Ola@gmail")
    customer.set_first_name("Ola")
    customer.set_last_name("Ola")
    booking_request.set_customer(customer)

    booking_request.set_room_type("single")
    booking_request.set_check_in_date("2023-07-17")
    booking_request.set_check_out_date("2023-07-20")

    return booking_request


def build_room():
    new_room = Room()
    new_room.set_room_type("single")
    new_room.set_room_price(4500)

    return new_room


class TestReservationServicesImplementation(TestCase):
    reservation_service = ReservationServicesImplementation()
    user_booking_request = build_booking_request()
    room = build_room()
    room_service = RoomServiceImplementation()

    def test_book_room(self):
        self.test_create_room()
        booked_room = self.reservation_service.book_room(self.user_booking_request)
        print(f"first Booking {booked_room} ")
        self.assertIsNotNone(booked_room)

        self.test_book_room_2()

    def test_create_room(self):
        saved_room = self.room_service.save_room(self.room)
        self.assertIsNotNone(saved_room)

        new_room2 = Room()
        new_room2.set_room_type("double")
        new_room2.set_room_price(4500)

        saved_room2 = self.room_service.save_room(new_room2)
        self.assertIsNotNone(saved_room2)

    def test_book_room_2(self):
        booking_request2 = BookRoomRequest()
        customer1 = Customer()
        customer1.set_email("Ola@gmail")
        customer1.set_first_name("timi")
        customer1.set_last_name("timi")
        booking_request2.set_customer(customer1)

        booking_request2.set_room_type("single")
        booking_request2.set_check_in_date("2023-07-21")
        booking_request2.set_check_out_date("2023-07-22")

        reservation2 = self.reservation_service.book_room(booking_request2)
        print(f"SECOND BOOKING {reservation2}")
        self.assertIsNotNone(reservation2)
