# add function which accepts any PaymentGateway object and calls its method (✅)
# add same function to 'get info' (⌛)
# customise 'get info' (⌛)


from abc import ABC, abstractmethod



class PaymentGateway(ABC):
    def __init__(self, number):
        self.__number = number



    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_status(self):
        pass



class CreditCard(PaymentGateway):
    def __init__(self, number, info):
        super().__init__(number)
        self.__info = info


    def process_payment(self, amount):
        # Тут має бути логіка перевірки amount
        if amount > 0:
            print(f"CreditCard processed {amount}$ successfully.")
            return True  # Успіх
        else:
            print(f"Cant processed less than 0$. Your amount is {amount}$")
            return False  # Невдача


    def get_status(self):
        print(f"Information about card: {self.__info}")



class PayPal(PaymentGateway):
    def __init__(self, number, user_info):
        super().__init__(number)
        self.__user_info = user_info


    def process_payment(self, amount):
        if amount > 10:
            print(f"PayPal processed {amount}$ successfully.")
            return True
        else:
            print(f"Cant processed less than 10$. Your amount is {amount}$")
            return False

    def get_status(self):
        print(f"User info: \n"
              f"name - {self.__user_info} \n")


# my_PayPal.get_status()

def make_order_payment(gateway: PaymentGateway, amount: int):   # Polymorphism

    print(f"\n--- Start processing via {gateway.__class__.__name__} ---")

    if gateway.process_payment(amount):
        print("Payment completed successfully.")
        return True
    else:
        print("The payment failed. Check the status.")
        gateway.get_status()
        return False




def main():

    while True:
        number = input("Enter your card number: ")

        if len(number) != 10:
            print("card contain only 10 digits")
            continue

        else:
            if number.isdigit():
                break
            else:
                print("only digits")
                continue


    while True:

        user_choice = input("Pick your payment method 'Credit Card' or 'PayPal' (CC / PP): ")

        if user_choice == "CC":
            while True:
                value = None
                try:
                    value = int(input("Enter amount to transfer: "))
                    break
                except ValueError:
                    print("Incorrect amount")
                    continue

            my_card = CreditCard(number, "VISA")  # tyt pomenyat
            return make_order_payment(my_card, value)

        elif user_choice == "PP":
            while True:
                value = None
                try:
                    value = int(input("Enter amount to transfer: "))
                    break
                except ValueError:
                    print("Incorrect amount")
                    continue

            my_paypal = PayPal(12345, "Dio23521")
            return make_order_payment(my_paypal, value)


        else:
            print("Wrong option")
            continue



if __name__ == '__main__':
    main()


