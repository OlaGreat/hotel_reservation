from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.model.Room import Room
from hotelReservation.data.repositories.customer_repository_implementation import CustomerRepositoryImplementation
from hotelReservation.dto.request.book_room_request import BookRoomRequest
from hotelReservation.dto.request.customer_registration_request import RegistrationRequest
from hotelReservation.dto.request.search_room_request import RoomSearchRequest
from hotelReservation.dto.response.registration_response import RegistrationResponse
from hotelReservation.services.customer_service import CustomerService
from hotelReservation.services.reservation_service_implementation import ReservationServicesImplementation


class CustomerReservationImplementation(CustomerService):
    customer_repo = CustomerRepositoryImplementation()
    reservation_service = ReservationServicesImplementation()

    def register(self, registration_request: RegistrationRequest):
        customer = Customer()
        customer.set_first_name(registration_request.get_first_name())
        customer.set_last_name(registration_request.get_last_name())
        customer.set_email(registration_request.get_email())
        saved_customer = self.customer_repo.save_customer(customer)

        if saved_customer is None:
            raise ValueError("Registration is unsuccessful please try registering again")

        response = RegistrationResponse()
        response.set_message(f"Dear {saved_customer.get_first_name()} {saved_customer.get_last_name()} your "
                             f"registration is successful")
        return saved_customer

    def search_for_room(self, search_request: RoomSearchRequest):
        room_type = search_request.get_room_type()
        check_in_date = search_request.get_check_in_date()
        check_out_date = search_request.get_check_out_date()

    def book_room(self, booking_request: BookRoomRequest):
        reserved_room = self.reservation_service.book_room(booking_request)
        if reserved_room is not None:
            customer_email = reserved_room.get_customer().get_email()
            customer = self.customer_repo.find_by_email(customer_email)
            customer.set_reservation(reserved_room)
            return f"Dear {customer.get_first_name} your room has been booked find below the details \n{reserved_room}"

        return None

    def view_customer_reservation(self, email):
        customer = self.customer_repo.find_by_email(email)
        if customer is not None:
            res = customer.get_reservation()
            for reservation in res:
                print(reservation)

    def find_customer_by_id(self, customer_id):
        return self.customer_repo.find_customer_by_id(customer_id)

    def delete_customer_by_id(self, customer_id):
        found_user = self.customer_repo.find_customer_by_id(customer_id)
        if found_user is not None:
            self.customer_repo.delete_customer_by_id(customer_id)
            return f"Customer successfully deleted"
        return f"No customer with such id {customer_id}"

    def get_all_customer(self):
        customer_list = self.customer_repo.get_all_customer()
        if len(customer_list) > 0:
            for customer in customer_list:
                print(customer)
        return f"there is no registered customer"
