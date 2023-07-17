from hotelReservation.data.model.Customer import Customer


class BookRoomRequest:

    def __init__(self):
        self.room_type = ""
        self.check_in_date = ""
        self.check_out_date = ""
        self.email = ""
        self.customer = Customer

    def set_check_in_date(self, checkin_date):
        self.check_in_date = checkin_date

    def get_check_in_date(self):
        return self.check_in_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    def get_check_out_date(self):
        return self.check_out_date

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_room_type(self):
        return self.room_type

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer
