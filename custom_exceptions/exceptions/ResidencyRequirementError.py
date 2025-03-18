from VoterEligibilityError import VoterEligibilityError


class ResidencyRequirementError(VoterEligibilityError):
    """Exception raised when voter does not meet residency requirements."""

    def __init__(self, residence_duration, required_duration):
        self.residence_duration = residence_duration
        self.required_duration = required_duration
        self.message = f"Residency requirement not met: {residence_duration} months (required: {required_duration} months)"
        super().__init__(self.message)
