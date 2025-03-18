from insurance import AutomobileInsurance, HealthInsurance

health_policy = HealthInsurance(
    "H123", "Alice Johnson", 500.0, 100000, "Family", True)
auto_policy = AutomobileInsurance(
    "A456", "Bob Smith", 300.0, "Car", "Toyota Corolla", "Comprehensive")

policies = [health_policy, auto_policy]

for policy in policies:
    print("\n--- Policy Details ---")
    policy.display_policy_details()
