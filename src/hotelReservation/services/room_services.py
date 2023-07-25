from abc import ABC, abstractmethod

from hotelReservation.data.model.Room import Room


class RoomServices(ABC):
    @abstractmethod
    def find_room(self, room_type, check_in_date, check_out_date):
        pass

    @abstractmethod
    def save_room(self, room: Room):
        pass

    @abstractmethod
    def delete_room(self, room_id:int):
        pass
