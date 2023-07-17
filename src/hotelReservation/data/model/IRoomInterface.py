from abc import ABC, abstractmethod


class IRoomInterface:

    @abstractmethod
    def set_room_number(self, room_number):
        pass

    @abstractmethod
    def set_room_type(self, room_type):
        pass

    @abstractmethod
    def set_room_price(self, room_price):
        pass

    @abstractmethod
    def get_room_number(self):
        pass

    @abstractmethod
    def get_room_price(self):
        pass

    @abstractmethod
    def get_room_type(self):
        pass
