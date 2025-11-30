
from abc import ABC, abstractmethod




class PaymentGateway(ABC):
    def __init__(self, amount):
        self.__amount = amount


    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_status(self):
        pass



class CreditCard(PaymentGateway):
    def __init__(self, number, info):
        super().__init__(self)
        self.__info = info
        self.__number = number

    def process_payment(self, amount):
        # Тут має бути логіка перевірки amount
        if amount > 0:
            print(f"CreditCard processed {amount}$ successfully.")
            return True  # Успіх
        return False  # Невдача

    def get_status(self):
        print(f"Інформація про картку: {self.__info}")



class PayPal(PaymentGateway):
    def __init__(self, user_info, balance):
        super().__init__(self)
        self.__user_info = user_info
        self.__balance = balance

    def process_payment(self, amount):
        if amount > 10:
            print(f"PayPal processed {amount}$ successfully.")
            return True
        print(f"Cant processed less than 10$. Your amount is {amount}$")
        return False

    def get_status(self):
        print(f"User info: \n"
              f"name - {self.__user_info} \n"
              f"balance - {self.__balance}$")


value = 100 # Сума транзакції
my_PayPal = PayPal("Dio23521", 500)
my_card = CreditCard(12345, "VISA")
# my_PayPal.get_status()
result = my_card.process_payment(value)

print(result)



