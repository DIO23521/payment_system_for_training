# add function which accepts any PaymentGateway object and calls its method (✅)
# add same function to 'get info' (⌛)
# customizable 'get info' (⌛)
# put "-" after every 4 number in card number (⌛)


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
        self.__number = number


    def process_payment(self, amount):
        # Тут має бути логіка перевірки amount
        if amount > 0:
            print(f"CreditCard processed {amount}$ successfully.")
            return True  # Успіх
        else:
            print(f"Cant processed less than 0$. Your amount is {amount}$")
            return False  # Невдача


    def get_status(self):
        print(f"Information about card: {self.__number} {self.__info}")



class PayPal(PaymentGateway):
    def __init__(self, number, user_info):
        super().__init__(number)
        self.__user_info = user_info
        self.__number = number


    def process_payment(self, amount):
        if amount > 10:
            print(f"PayPal processed {amount}$ successfully.")
            return True
        else:
            print(f"Cant processed less than 10$. Your amount is {amount}$")
            return False

    def get_status(self):
        print(f"User info: \n"
              f"name - {self.__user_info} \n"
              f"№ - {self.__number}")


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



def make_depo_cc():
    while True:
        value = None
        try:
            value = int(input("Enter amount to transfer: "))
            break
        except ValueError:
            print("Incorrect amount")
            continue

    my_card = CreditCard(12345, "VISA")
    payment_successful = make_order_payment(my_card, value)
    return value if payment_successful else 0


def make_depo_pp():
    while True:
        value = None
        try:
            value = int(input("Enter amount to transfer: "))
            break
        except ValueError:
            print("Incorrect amount")
            continue

    my_paypal = PayPal(12345, "Dio23521")
    payment_successful2 = make_order_payment(my_paypal, value)
    return value if payment_successful2 else 0

def get_information():
    gate_instance = None
    while True:
        info_choice = input("For what system you want information (CC/PP): ").upper()
        if info_choice == "CC":
            gate_instance = CreditCard(12345, "VISA")
            break
        elif info_choice == "PP":
            gate_instance = PayPal(12345, "Dio23521")
            break
        else:
            continue
    print(f"\n--- Start processing via {gate_instance.__class__.__name__} ---")
    gate_instance.get_status()




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

    cc_balance = 0
    pp_balance = 0

    while True:
        print("\n1. Show balance")
        print("2. Credit Card deposit")
        print("3. Pay Pal deposit")
        print("4. Withdraw")
        print("5. Exit")
        print("6. status")
        answer = input("Select option: ")

        if answer == "1":
            while True:
                balance_option = input("Pick balance that you want to see 'Credit Card' or 'PayPal' (CC/PP): ").upper()
                if balance_option == "CC":
                    print(cc_balance)
                    break
                elif balance_option == "PP":
                    print(pp_balance)
                    break
                else:
                    print("Wrong option")
                    continue

        elif answer == "2":
            cc_balance += make_depo_cc()
        elif answer == "3":
            pp_balance += make_depo_pp()
        elif answer == "4":
            pass
        elif answer == "5":
            print("Bye")
            break
        elif answer == "6":
            get_information()
        else:
            print("---------------------")
            print("   Invalid choice.   "
                  "   Select from 1-4   ")
            print("---------------------")






if __name__ == '__main__':
    main()


