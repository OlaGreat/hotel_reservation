from datetime import datetime, timedelta

from hotelReservation.data.model import Customer, Room


class Reservation:
    def __init__(self):
        self.customer = Customer
        self.room = Room
        self.check_in_date: datetime = datetime.today()
        self.check_out_date: datetime = datetime(1, 1, 1)
        self.reservation_id: int = 0

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def get_reservation_id(self):
        return self.reservation_id

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer

    def set_room(self, room):
        self.room = room

    def get_room(self):
        return self.room

    def set_check_in_date(self, check_in_date):
        self.check_in_date = self.convert_to_local_date(check_in_date)

    def get_check_in_date(self):
        return self.check_in_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = self.convert_to_local_date(check_out_date)

    def get_check_out_date(self):
        return self.check_out_date

    def convert_to_local_date(self, date_string):
        date_format = "%Y-%m-%d"  # Specify the format of your date string
        date = datetime.strptime(date_string, date_format)  # Parse the date string to a datetime object
        local_date = date.strftime(date_format)  # Convert the datetime object to local date string
        return local_date

    def __str__(self):
        return f" {self.customer}\n {self.room} \n check_in_date ->{self.check_in_date}\n" \
               f"check_out_date -> {self.check_out_date}"
