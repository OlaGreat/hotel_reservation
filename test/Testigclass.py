import unittest

from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.Room_repository_implementation import RoomRepositoryImplementation


class Tester(unittest.TestCase):

    new_room = None

    @classmethod
    def setUp(cls) -> None:
        cls.room_repository = RoomRepositoryImplementation()
        cls.new_room = Room()
        cls.new_room.set_room_price(4500)
        cls.new_room.set_room_type("Single")

    def test_save_method(self):
        saved_room = self.room_repository.save(self.new_room)
        self.assertIsNotNone(saved_room)

    def test_stuffs(self):
        self.assertEqual(1, 1)
