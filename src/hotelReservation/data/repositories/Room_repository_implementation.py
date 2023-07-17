from datetime import datetime, date

from hotelReservation.AppUtils.Utils import Utils
from hotelReservation.data.model.FreeRoom import FreeRoom
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.Room_repository import RoomRepository


class RoomRepositoryImplementation(RoomRepository):

    def __init__(self):
        self.rooms = []

    def save_room(self, room: Room):
        room.set_room_number(Utils.generate_id())
        self.rooms.append(room)
        return room

    def save_free_room(self, room: FreeRoom):
        room.set_room_number(Utils.generate_id())
        self.rooms.append(room)
        return room

    def find_room_by_id(self, room_number):
        for room in self.rooms:
            if room.get_room_number() == room_number:
                return room

        return None

    def delete_room_by_room_id(self, room_number):
        found_room = self.find_room_by_id(room_number)
        if found_room is not None:
            self.rooms.remove(found_room)

        else:
            return "No room with such number"

    def get_all_room(self):
        return self.rooms

    def find_room(self, room_type, check_in_date, check_out_date):
        in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        if in_date < datetime.today():
            raise ValueError(f"date cant be less than {date.today()}")
        for room in self.rooms:
            if room.get_room_type() is room_type:
                if room.get_is_booked() is False:
                    room.set_is_booked(True)
                    return room

        return None
