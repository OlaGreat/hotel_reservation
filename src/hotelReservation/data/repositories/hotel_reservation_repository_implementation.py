from datetime import datetime, date

from hotelReservation.AppUtils.Utils import Utils
from hotelReservation.data.model.Reservation import Reservation
from hotelReservation.data.repositories.hotel_reservation_repository import HotelReservation


class HotelReservationImplementation(HotelReservation):

    def __init__(self):
        self.reservation_list = []

    def save_reservation(self, reservation: Reservation):
        reservation.set_reservation_id(Utils.generate_id())
        self.reservation_list.append(reservation)
        return reservation

    def find_reservation_by_id(self, reservation_id):
        for reservation in self.reservation_list:
            if reservation.get_reservation_id() == reservation_id:
                return reservation
        print(f"No Reservation with the id {reservation_id}")
        return None

    def delete_reservation_by_id(self, reservation_id):
        found_reservation = self.find_reservation_by_id(reservation_id)
        if found_reservation is not None:
            self.reservation_list.remove(found_reservation)

    def get_all(self):
        return self.reservation_list

    def search_reservation(self, room_type, check_in_date, check_out_date):
        in_day = datetime.strptime(check_in_date, "%Y-%m-%d")
        out_day = datetime.strptime(check_out_date, "%Y-%m-%d")
        if in_day < datetime.today() or out_day < datetime.today():
            raise ValueError(f"date cant be less than {date.today()}")

        for reservation in self.reservation_list:
            if reservation.get_room().get_room_type() == room_type:
                if check_in_date < reservation.get_check_in_date() or check_in_date > reservation.get_check_out_date():
                    if check_out_date < reservation.get_check_in_date():
                        return reservation
                    elif check_in_date > reservation.get_check_out_date() and check_out_date > reservation.get_check_out_date():
                        return reservation
        return None

    # def search_reservation(self, room_type, check_in_date, check_out_date):
    # if check_in_date or check_out_date < datetime.today():
    #     raise ValueError(f"date cant be less than {date.today()}")
    #     for reservation in self.reservation_list:
    #         if reservation.get_room().get_room_type() == room_type:
    #             if (check_in_date > reservation.get_check_out_date()) or (
    #                     check_out_date < reservation.get_check_in_date()):
    #                 return reservation
    #     return None
