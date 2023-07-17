from hotelReservation.AppUtils.Utils import Utils
from hotelReservation.data.model.Customer import Customer
from hotelReservation.data.repositories.customer_Repository import CustomerRepository


class CustomerRepositoryImplementation(CustomerRepository):

    def __init__(self):
        self.customer_list = []

    def save_customer(self, customer: Customer):
        customer.set_customer_id(Utils.generate_id())
        self.customer_list.append(customer)
        return customer

    def find_customer_by_id(self, customer_id):
        for customer in self.customer_list:
            if customer.get_customer_id() == customer_id:
                return customer
        print(f"No customer with id {customer_id} ")
        return None

    def delete_customer_by_id(self, customer_id):
        found_user = self.find_customer_by_id(customer_id)
        if found_user is not None:
            self.customer_list.remove(found_user)

    def get_all_customer(self):
        return self.customer_list

    def find_by_email(self, email):
        for customer in self.customer_list:
            if customer.get_email() == email:
                return customer

        return None
