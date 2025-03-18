from VoterEligibilityError import VoterEligibilityError

class RegistrationError(VoterEligibilityError):
    """Exception raised when voter is not registered in the system."""

    def __init__(self, voter_id=None):
        self.voter_id = voter_id
        id_info = f" (ID: {voter_id})" if voter_id else ""
        self.message = f"Voter is not registered in the system{id_info}"
        super().__init__(self.message)
