from abc import ABC, abstractmethod

from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest


class ReservationServices(ABC):
    @abstractmethod
    def search_reservation(self, search_request: RoomSearchRequest):
        pass

    @abstractmethod
    def search_for_room(self, search_request: RoomSearchRequest):
        pass

    @abstractmethod
    def book_room(self, booking_request: BookRoomRequest):
        pass
