from insurance import Insurance

# class ChildClass(ParentClass):
#     pass

class HealthInsurance(Insurance):
    def __init__(self, policy_number: str, customer_name: str, insured_amount: float,
                 coverage_amount: float, plan_type: str, pre_existing_conditions: bool):
        # Call the base class __init__ method
        # The super() function in Python calls a method from the parent class
        super().__init__(policy_number, customer_name, insured_amount)
        print("__init__ of HealthInsurance")
        self._coverage_amount = coverage_amount
        self._plan_type = plan_type
        self._pre_existing_conditions = pre_existing_conditions

    # Getters and Setters
    def get_coverage_amount(self) -> float:
        return self._coverage_amount

    def set_coverage_amount(self, amount: float):
        if amount < 0:
            raise ValueError("Coverage amount cannot be negative")
        self._coverage_amount = amount

    def get_plan_type(self) -> str:
        return self._plan_type

    def set_plan_type(self, plan_type: str):
        self._plan_type = plan_type

    def has_pre_existing_conditions(self) -> bool:
        return self._pre_existing_conditions

    def set_pre_existing_conditions(self, has_conditions: bool):
        self._pre_existing_conditions = has_conditions

    # Method overriding
    def display_policy_details(self) -> None:
      """Overridden method to display Health Insurance specific details"""
      super().display_policy_details()
      print(f"Coverage Amount: ${self._coverage_amount:.2f}")
      print(f"Plan Type: {self._plan_type}")
      print(f"Pre-existing Conditions: {'Yes' if self._pre_existing_conditions else 'No'}")
