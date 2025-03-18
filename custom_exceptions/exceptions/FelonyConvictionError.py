from VoterEligibilityError import VoterEligibilityError

class FelonyConvictionError(VoterEligibilityError):
    """Exception raised when voter has disqualifying criminal record."""

    def __init__(self, offense_type=None):
        self.offense_type = offense_type
        offense_info = f" for {offense_type}" if offense_type else ""
        self.message = f"Voting rights restricted due to felony conviction{offense_info}"
        super().__init__(self.message)
