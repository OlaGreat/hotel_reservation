class Admin:
    def __init__(self):
        self.admin_id = 0
        self.first_name = ""
        self.last_name = ""
        self.email = ""

    def set_admin_id(self, admin_id):
        self.admin_id = admin_id

    def get_admin_id(self):
        return self.admin_id

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

    def __str__(self):
        return f"first_name --> {self.first_name}\n last_name -->{self.last_name}\n email==> {self.email} "
