class Utils:
    rooms_number = 0

    @staticmethod
    def generate_id():
        Utils.rooms_number += 1
        return Utils.rooms_number
