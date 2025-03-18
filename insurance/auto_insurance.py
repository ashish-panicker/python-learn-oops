from insurance import Insurance

# Derived class for Automobile Insurance

class AutomobileInsurance(Insurance):
    def __init__(self, policy_number: str, customer_name: str, insured_amount: float,
                 vehicle_type: str, vehicle_model: str, coverage_type: str):
        super().__init__(policy_number, customer_name, insured_amount)
        print("__init__ of AutomobileInsurance")
        self._vehicle_type = vehicle_type
        self._vehicle_model = vehicle_model
        self._coverage_type = coverage_type

    # Getters and Setters
    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def set_vehicle_type(self, vehicle_type: str):
        self._vehicle_type = vehicle_type

    def get_vehicle_model(self) -> str:
        return self._vehicle_model

    def set_vehicle_model(self, vehicle_model: str):
        self._vehicle_model = vehicle_model

    def get_coverage_type(self) -> str:
        return self._coverage_type

    def set_coverage_type(self, coverage_type: str):
        self._coverage_type = coverage_type

    def display_policy_details(self) -> None:
        """Overridden method to display Automobile Insurance specific details"""
        super().display_policy_details()
        print(f"Vehicle Type: {self._vehicle_type}")
        print(f"Vehicle Model: {self._vehicle_model}")
        print(f"Coverage Type: {self._coverage_type}")
