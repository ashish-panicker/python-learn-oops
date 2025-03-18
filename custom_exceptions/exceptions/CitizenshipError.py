from VoterEligibilityError import VoterEligibilityError

class CitizenshipError(VoterEligibilityError):
    """Exception raised when voter is not a citizen."""

    def __init__(self, nationality):
        self.nationality = nationality
        self.message = f"Citizenship requirement not met: Current nationality is {nationality}"
        super().__init__(self.message)
