from VoterEligibilityError import VoterEligibilityError

class AgeRequirementError(VoterEligibilityError):
    """Exception raised when voter does not meet the minimum age requirement."""

    def __init__(self, age, min_age=18):
        self.age = age
        self.min_age = min_age
        self.message = f"Age requirement not met: {age} years old (minimum required: {min_age} years)"
        super().__init__(self.message)
