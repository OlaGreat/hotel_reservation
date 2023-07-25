from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.Room_repository_implementation import RoomRepositoryImplementation
from hotelReservation.services.room_services import RoomServices


class RoomServiceImplementation(RoomServices):
    room_repo = RoomRepositoryImplementation()

    def save_room(self, room: Room):
        return self.room_repo.save_room(room)

    def find_room(self, room_type, check_in_date, check_out_date):
        return self.room_repo.find_room(room_type, check_in_date, check_out_date)

    def delete_room(self, room_id: int):
        self.room_repo.delete_room_by_room_id(room_id)
