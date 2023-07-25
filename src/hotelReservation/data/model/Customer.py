from hotelReservation.data.model.Reservation import Reservation


class Customer:
    def __init__(self):
        self.first_name: str = ""
        self.last_name: str = ""
        self.email: str = ""
        self.customer_id = 0
        self.reservation_list = []

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_reservation(self, reservation: Reservation):
        self.reservation_list.append(reservation)

    def get_reservation(self):
        return self.reservation_list

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id

    def __str__(self):
        return f" firstName -> {self.first_name}\n last_name-> {self.first_name}\n email --> {self.email}\n"
