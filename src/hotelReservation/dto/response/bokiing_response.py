class ReservationResponse:
    def __init__(self):
        self.message = ""

    def set_message(self, message):
        self.message = message
        
    def get_message(self):
        return self.message


