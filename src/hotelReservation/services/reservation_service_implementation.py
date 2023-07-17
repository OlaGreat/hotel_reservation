from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Reservation import Reservation
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.hotel_reservation_repository_implementation import \
    HotelReservationImplementation
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest
from hotelReservation.services.reservation_service import ReservationServices
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


class ReservationServicesImplementation(ReservationServices):
    reservation_repo = HotelReservationImplementation()
    room_service = RoomServiceImplementation()

    def search_for_room(self, search_request: RoomSearchRequest):
        room_type = search_request.get_room_type()
        check_in_date = search_request.get_check_in_date()
        check_out_date = search_request.get_check_out_date()
        return self.room_service.find_room(room_type, check_in_date, check_out_date)

    def book_room(self, booking_request: BookRoomRequest):
        search_request = RoomSearchRequest()
        search_request.set_room_type(booking_request.get_room_type())
        search_request.set_checkin_date(booking_request.get_check_in_date())
        search_request.set_check_out_date(booking_request.get_check_out_date())
        found_room = self.search_for_room(search_request)
        if found_room is None:
            new_found_room = self.reservation_repo.search_reservation(booking_request.get_room_type(),
                                                                      booking_request.get_check_in_date(),
                                                                      booking_request.get_check_out_date())
            if new_found_room is not None:
                new_reservation = Reservation()
                customer = Customer()
                customer.set_first_name(booking_request.get_customer().get_first_name())
                customer.set_last_name(booking_request.get_customer().get_email())
                customer.set_email(booking_request.get_customer().get_email())
                new_reservation.set_customer(customer)
                new_reservation.set_room(new_found_room.get_room())
                new_reservation.set_check_in_date(booking_request.get_check_in_date())
                new_reservation.set_check_out_date(booking_request.get_check_out_date())
                reserved = self.reservation_repo.save_reservation(new_reservation)
                return reserved
            else:
                return None
        else:
            new_reservation = Reservation()
            customer = Customer()
            room = Room()
            customer.set_first_name(booking_request.get_customer().get_first_name())
            customer.set_last_name(booking_request.get_customer().get_last_name())
            customer.set_email(booking_request.get_customer().get_email())
            new_reservation.set_customer(customer)

            room.set_room_number(found_room.get_room_number())
            room.set_room_type(found_room.get_room_type())
            room.set_room_price(found_room.get_room_price())
            new_reservation.set_room(room)

            new_reservation.set_check_in_date(booking_request.get_check_in_date())
            new_reservation.set_check_out_date(booking_request.get_check_out_date())
            made_reservation = self.reservation_repo.save_reservation(new_reservation)
            return made_reservation

    def search_reservation(self, search_request: RoomSearchRequest):
        room_type = search_request.get_room_type()
        check_in_date = search_request.get_check_in_date()
        check_out_date = search_request.get_check_out_date()
