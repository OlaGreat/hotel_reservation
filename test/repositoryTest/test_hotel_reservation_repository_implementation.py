from datetime import date, timedelta
from unittest import TestCase

from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Reservation import Reservation
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.hotel_reservation_repository_implementation import \
    HotelReservationRepositoryImplementation


def build_reservation():
    reservation = Reservation()
    booked_room = Room()
    booked_room.set_room_number(1)
    booked_room.set_room_price(4500)
    booked_room.set_room_type("single")
    reservation.set_room(booked_room)

    customer = Customer()
    customer.set_email("Ola@gmail.com")
    customer.set_last_name("Ola")
    customer.set_first_name("Ola")
    reservation.set_customer(customer)
    reservation.set_check_in_date("2023-07-17")
    reservation.set_check_out_date("2023-07-21")

    return reservation


class TestHotelReservationImplementation(TestCase):
    reservation_repo = HotelReservationRepositoryImplementation()
    reserved = build_reservation()

    def test_save_reservation(self):
        saved_reservation = self.reservation_repo.save_reservation(self.reserved)
        self.assertIsNotNone(saved_reservation)

    def test_find_reservation_by_id(self):
        saved_reservation = self.reservation_repo.save_reservation(self.reserved)
        self.assertIsNotNone(saved_reservation)
        found_reservation = self.reservation_repo.find_reservation_by_id(saved_reservation.get_reservation_id())
        self.assertIsNotNone(found_reservation)

    def test_delete_reservation_by_id(self):
        saved_reservation = self.reservation_repo.save_reservation(self.reserved)
        self.assertIsNotNone(saved_reservation)
        self.reservation_repo.delete_reservation_by_id(saved_reservation.get_reservation_id())
        self.assertEqual(0, len(self.reservation_repo.get_all()))

    def test_search_room(self):
        saved_reservation = self.reservation_repo.save_reservation(self.reserved)
        self.assertIsNotNone(saved_reservation)
        # reservation.set_check_in_date("2023-07-17")
        # reservation.set_check_out_date("2023-07-21")
        found_reservation = self.reservation_repo.search_reservation("single", "2023-07-25", "2023-07-22")
        self.assertIsNotNone(found_reservation)
        print(found_reservation)
