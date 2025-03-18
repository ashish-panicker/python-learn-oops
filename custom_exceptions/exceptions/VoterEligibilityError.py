
# Inherit from the Exception class
class VoterEligibilityError(Exception):
    """Base exception class for all voter eligibility related errors."""

    def __init__(self, message="Voter eligibility error"):
        super().__init__(self.message)
        self.message = message
