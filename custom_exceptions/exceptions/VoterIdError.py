
from VoterEligibilityError import VoterEligibilityError


class VoterIdError(VoterEligibilityError):
    """Exception raised when voter lacks proper identification."""

    def __init__(self, missing_documents=None):
        self.missing_documents = missing_documents or []
        docs_info = f": Missing {', '.join(self.missing_documents)}" if self.missing_documents else ""
        self.message = f"Voter identification requirements not met{docs_info}"
        super().__init__(self.message)
