from hotelReservation.data.model import IRoomInterface


class FreeRoom:
    def __init__(self):
        self.room_number: int = 0
        self.room_price = 0

    def get_free_room_price(self):
        return self.room_price

    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_number(self):
        return self.room_number
