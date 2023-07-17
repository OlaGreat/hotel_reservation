from abc import ABC, abstractmethod


class CustomerRepository(ABC):
    @abstractmethod
    def save_customer(self, customer):
        pass

    @abstractmethod
    def find_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def get_all_customer(self):
        pass

    @abstractmethod
    def find_by_email(self, email):
        pass
