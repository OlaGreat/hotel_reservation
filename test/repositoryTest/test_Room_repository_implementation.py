import unittest

from hotelReservation.data.model.FreeRoom import FreeRoom
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.Room_repository_implementation import RoomRepositoryImplementation


class TestRoomRepositoryImplementation(unittest.TestCase):
    room_repo = RoomRepositoryImplementation()

    def test_save_method(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)

        saved_room = self.room_repo.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = FreeRoom()
        saved_free_room = self.room_repo.save_free_room(new_room1)
        self.assertIsNotNone(saved_free_room)

    def test_get_all_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)

        saved_room = self.room_repo.save_room(new_room)
        self.assertIsNotNone(saved_room)
        room_length = self.room_repo.get_all_room()
        self.assertEqual(len(room_length), len(self.room_repo.get_all_room()))

    def test_find_room_by_id(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_repo.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("SINGLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_repo.save_room(new_room1)
        self.assertIsNotNone(saved_room1)

        found_room = self.room_repo.find_room_by_id(saved_room.get_room_number())
        self.assertIsNotNone(found_room)
        self.assertEqual(found_room, saved_room)

    def test_delete_room_by_id(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_repo.save_room(new_room)
        self.assertIsNotNone(saved_room)

        self.room_repo.delete_room_by_room_id(saved_room.get_room_number())

        self.assertEqual(0, len(self.room_repo.get_all_room()))

    def test_find_room(self):
        new_room = Room()
        new_room.set_room_type("SINGLE")
        new_room.set_room_price(4500)
        saved_room = self.room_repo.save_room(new_room)
        self.assertIsNotNone(saved_room)

        new_room1 = Room()
        new_room1.set_room_type("DOUBLE")
        new_room1.set_room_price(4500)
        saved_room1 = self.room_repo.save_room(new_room1)
        self.assertIsNotNone(saved_room1)

        new_room2 = Room()
        new_room2.set_room_type("SINGLE")
        new_room2.set_room_price(4500)
        saved_room2 = self.room_repo.save_room(new_room2)
        self.assertIsNotNone(saved_room2)

        found_room = self.room_repo.find_room("DOUBLE", "2023-07-14", "2023-07-15")
        # self.assertIsNotNone(found_room)
        print(found_room)

