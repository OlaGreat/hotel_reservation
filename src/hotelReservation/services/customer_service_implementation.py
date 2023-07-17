from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.customer_repository_implementation import CustomerRepositoryImplementation
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest
from hotelReservation.dto.response.registration_response import RegistrationResponse
from hotelReservation.services.customer_service import CustomerService
from hotelReservation.services.reservation_service_implementation import ReservationServicesImplementation
from hotelReservation.services.room_service_implementation import RoomServiceImplementation


class CustomerReservationImplementation(CustomerService):
    customer_repo = CustomerRepositoryImplementation()
    room_service = RoomServiceImplementation()
    reservation_service = ReservationServicesImplementation()

    def register(self, registration_request: RegistrationRequest):
        customer = Customer()
        customer.set_first_name(registration_request.get_first_name())
        customer.set_last_name(registration_request.get_last_name())
        customer.set_email(registration_request.get_email())

        if customer is not None:
            saved_customer = self.customer_repo.save_customer(customer)

        response = RegistrationResponse()
        response.set_message(f"Dear {saved_customer.get_first_name()} {saved_customer.get_last_name()} your "
                             f"registration is successful")

        return response

    def search_for_room(self, search_request: RoomSearchRequest):
        room_type = search_request.get_room_type()
        check_in_date = search_request.get_check_in_date()
        check_out_date = search_request.get_check_out_date()
        return self.room_service.find_room(room_type, check_in_date, check_out_date)

    def book_room(self, booking_request: BookRoomRequest):
        found_room: Room()
        search_request = RoomSearchRequest()
        search_request.set_room_type(booking_request.get_room_type())
        search_request.set_checkin_date(booking_request.get_check_in_date())
        search_request.set_check_out_date(booking_request.get_check_out_date())
        found_room = self.search_for_room(search_request)
        if found_room is None:
            new_found_room = self.reservation_service.search_reservation(search_request)

    def view_reservation(self):
        pass

    def find_customer_by_id(self, customer_id):
        pass

    def delete_customer_by_id(self, customer_id):
        pass

    def get_all_customer(self):
        return self.customer_repo.get_all_customer()
