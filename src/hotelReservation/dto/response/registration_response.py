class RegistrationResponse:
    def __init__(self):
        self.message: str = ""

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def __str__(self):
        return f"{self.message}"
