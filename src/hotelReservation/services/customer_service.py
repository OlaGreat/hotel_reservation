from abc import ABC, abstractmethod

from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest


class CustomerService(ABC):
    @abstractmethod
    def register(self, registration_request: RegistrationRequest):
        pass

    @abstractmethod
    def search_for_room(self, search_request: RoomSearchRequest):
        pass

    @abstractmethod
    def book_room(self, booking_request: BookRoomRequest):
        pass

    @abstractmethod
    def view_customer_reservation(self, email: str):
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id: int):
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int):
        pass

    @abstractmethod
    def get_all_customer(self):
        pass
