from abc import ABC, abstractmethod


class HotelReservation(ABC):
    @abstractmethod
    def save_reservation(self, reservation):
        pass

    @abstractmethod
    def find_reservation_by_id(self, reservation_id):
        pass

    @abstractmethod
    def delete_reservation_by_id(self, reservation_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def search_reservation(self, room_type, check_in_date, check_out_date):
        pass
