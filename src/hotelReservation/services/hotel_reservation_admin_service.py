from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room
from hotelReservation.services.admin_service import AdminService
from hotelReservation.services.customer_service_implementation import CustomerReservationImplementation
from hotelReservation.services.reservation_service_implementation import ReservationServicesImplementation
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


class HotelReservationAdminService(AdminService):
    customer_services = CustomerReservationImplementation()
    reservation_service = ReservationServicesImplementation()
    room_service = RoomServiceImplementation()

    def get_all_customers(self) -> []:
        customers = []
        hotel_customers = self.customer_services.get_all_customer()
        if len(hotel_customers) > 0:
            for customer in hotel_customers:
                return customer
        return None

    def display_all_reservations(self) -> []:
        all_reservation = []
        reservations = self.reservation_service.get_all_reservation()
        return reservations

    def get_customer(self, customer_email: str) -> Customer:
        return self.customer_services.get_customer_by_email(customer_email)

    def add_room(self, room: Room):
        return self.room_service.save_room(room)

    def get_all_rooms(self) -> []:
        return self.room_service.get_all_room()
