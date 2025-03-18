from datetime import datetime

class BankAccount:
    # Class level or global attributes
    bank_name = "ABC Bank"
    bank_ifsc_code = ""

    def __init__(self, account_holder:str, balance:float=0.0):
        self.account_holder = account_holder
        self.balance = balance

    # Instance
    def print_details(self):
        print(f"Account Holder {self.account_holder}, Balance {self.balance}")

    def __str__(self):
        return f"Account Holder {self.account_holder}, Balance {self.balance}"

    @classmethod                                            # annotate with @classmethod
    def change_bank_name(cls, new_bank_name: str):          # first argument is cls
        old_bank_name = cls.bank_name
        cls.bank_name = new_bank_name                       # use cls to access the class attributes
        return f"Bank name updated from {old_bank_name} to {new_bank_name}"

    # Alternative constructor
    @classmethod
    def account_from_string(cls, account_str:str):
        print(cls)
        account_holder, balance = account_str.split("-")
        return cls(account_holder, balance)

    @staticmethod
    def check_if_deposit_allowed(date_string):
        date_obj = datetime.strptime(date_string, "%d-%m-%Y")
        if date_obj.weekday() >= 5 :
            print(f"No deposit allowed on {date_obj.weekday()} day of the week.")
        else:
            print(f"Deposit allowed on {date_obj.weekday() + 1} day of the week.")

arun = BankAccount("Arun", 3400)
print(arun, arun.bank_name)
print(BankAccount.change_bank_name("Universal Bank"))
print(arun, arun.bank_name)
print(BankAccount.check_if_deposit_allowed("10-03-2025"))
print(BankAccount.account_from_string("ashish-2000.0"))