from abc import ABC, abstractmethod
from datetime import datetime


class RoomRepository(ABC):
    @abstractmethod
    def save_room(self, room):
        pass

    @abstractmethod
    def save_free_room(self, room):
        pass

    @abstractmethod
    def find_room_by_id(self, room_number):
        pass

    @abstractmethod
    def delete_room_by_room_id(self, room_number):
        pass

    @abstractmethod
    def get_all_room(self):
        pass

    @abstractmethod
    def find_room(self, room_type, check_in_date, check_out_date):
        pass
