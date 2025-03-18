"""
A company provides insurance policies for both health and automobiles. While all insurance policies share 
common attributes like policy number, policyholder name, and premium amount, the details vary based 
on the type of insurance.

Health Insurance includes attributes like coverage amount, type of plan (individual/family), and pre-existing conditions.
Automobile Insurance includes attributes like vehicle type, vehicle model, and coverage type (comprehensive/third-party).
"""

class Insurance:
    def __init__(self, policy_number: str, customer_name: str, insured_amount: float):
        print("__init__ of Insurance")
        self._policy_number = policy_number  # Encapsulated attribute
        self._customer_name = customer_name
        self._insured_amount = insured_amount

    # Getters and Setters for Encapsulation
    def get_policy_number(self) -> str:       # -> str, return type annotation
        return self._policy_number

    def set_policy_number(self, policy_number: str):
        self._policy_number = policy_number

    def get_customer_name(self) -> str:
        return self._customer_name

    def set_customer_name(self, name: str):
        self._customer_name = name

    def get_insured_amount(self) -> float:
        return self._insured_amount

    def set_insured_amount(self, amount: float):
        if amount < 0:
            raise ValueError("Insured amount cannot be negative")
        self._insured_amount = amount

    def display_policy_details(self) -> None:
      """Common method for displaying policy details"""
      print(f"Policy Number: {self._policy_number}")
      print(f"Customer Name: {self._customer_name}")
      print(f"Insured Amount: ${self._insured_amount:.2f}")
