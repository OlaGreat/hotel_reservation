class RoomSearchRequest:

    def __init__(self):
        self.check_in_date = ""
        self.checking_out_date = ""
        self.room_Type = ""

    def set_checkin_date(self, checkin_date):
        self.check_in_date = checkin_date

    def get_check_in_date(self):
        return self.check_in_date

    def set_check_out_date(self, check_out_date):
        self.checking_out_date = check_out_date

    def get_check_out_date(self):
        return self.checking_out_date

    def set_room_type(self, room_type):
        self.room_Type = room_type

    def get_room_type(self):
        return self.room_Type
