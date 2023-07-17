from unittest import TestCase

from hotelReservation.data.model.Room import Room
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


class TestRoomServiceImplementation(TestCase):
    room_serv = RoomServiceImplementation()

    def test_save_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_serv.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("DOUBLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_serv.save_room(new_room1)
        self.assertIsNotNone(saved_room1)

        new_room2 = Room()
        new_room2.set_room_type("SINGLE")
        new_room2.set_room_price(4500)
        saved_room2 = self.room_serv.save_room(new_room2)
        self.assertIsNotNone(saved_room2)

    def test_find_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_serv.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("DOUBLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_serv.save_room(new_room1)
        self.assertIsNotNone(saved_room1)

        new_room2 = Room()
        new_room2.set_room_type("SINGLE")
        new_room2.set_room_price(4500)
        saved_room2 = self.room_serv.save_room(new_room2)
        self.assertIsNotNone(saved_room2)

        found_room = self.room_serv.find_room("SINGLE", "2023-07-20", "2023-07-14")
        self.assertIsNotNone(found_room)

