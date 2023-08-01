from abc import ABC, abstractmethod

from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room


class AdminService(ABC):
    @abstractmethod
    def get_customer(self, customer_email: str) -> Customer:
        pass

    @abstractmethod
    def add_room(self, room: Room) -> Room:
        pass

    @abstractmethod
    def get_all_rooms(self) -> []:
        pass

    @abstractmethod
    def get_all_customers(self) -> []:
        pass

    @abstractmethod
    def display_all_reservations(self) -> []:
        pass
