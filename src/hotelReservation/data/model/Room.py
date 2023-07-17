from hotelReservation.data.model import Room_Type


class Room:

    def __init__(self):
        self.room_type = Room_Type
        self.room_price: int = 0
        self.room_number: int = 0
        self.is_booked = False

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_room_type(self):
        return self.room_type

    def set_room_price(self, room_price):
        self.room_price = room_price

    def get_room_price(self):
        return self.room_price

    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_number(self):
        return self.room_number

    def set_is_booked(self, state: bool):
        self.is_booked = state

    def get_is_booked(self):
        return self.is_booked

    def __str__(self):
        return f"RoomType -> {self.room_type}\nRoomPrice -> {self.room_price}\n" \
               f"RoomNumber -> {self.room_number}\n"
