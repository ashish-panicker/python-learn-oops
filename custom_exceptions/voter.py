from exceptions import VoterIdError, AgeRequirementError, CitizenshipError, FelonyConvictionError, RegistrationError, ResidencyRequirementError, VoterEligibilityError


class VoterRegistry:
    """Voter registration and eligibility verification system."""

    def __init__(self, residency_requirement=6, voter_id_required=True):
        self.voters = {}
        self.residency_requirement = residency_requirement  # in months
        self.voter_id_required = voter_id_required

    def register_voter(self, voter_id, name, age, is_citizen, residence_duration,
                       has_felony=False, id_documents=None):
        """Register a new voter in the system."""
        self.voters[voter_id] = {
            'name': name,
            'age': age,
            'is_citizen': is_citizen,
            'residence_duration': residence_duration,
            'has_felony': has_felony,
            'id_documents': id_documents or []
        }
        return f"Voter {name} registered with ID: {voter_id}"

    def check_eligibility(self, voter_id):
        """
        Check if a voter is eligible to vote.
        Raises appropriate exceptions if any eligibility criteria are not met.
        """
        # Check if voter is registered
        if voter_id not in self.voters:
            raise RegistrationError(voter_id)

        voter = self.voters[voter_id]

        # Check age requirement
        if voter['age'] < 18:
            raise AgeRequirementError(voter['age'])

        # Check citizenship
        if not voter['is_citizen']:
            raise CitizenshipError(nationality="Non-citizen")

        # Check residency requirement
        if voter['residence_duration'] < self.residency_requirement:
            raise ResidencyRequirementError(
                voter['residence_duration'], self.residency_requirement)

        # Check for felony conviction
        if voter['has_felony']:
            raise FelonyConvictionError()

        # Check for voter ID if required
        if self.voter_id_required and not voter['id_documents']:
            raise VoterIdError(["government-issued photo ID"])

        # If all checks pass
        return True
    
    def can_vote(self, voter_id):
      """
      Determine if a voter can vote, returning a result instead of raising exceptions.
      Returns a tuple: (is_eligible, message)
      """
      try:
          self.check_eligibility(voter_id)
          return True, f"Voter {voter_id} is eligible to vote."
      except VoterEligibilityError as e:
          return False, str(e)


def main():
    # Create a voter registry
    registry = VoterRegistry(residency_requirement=6)

    # Register some voters
    registry.register_voter("V001", "John Doe", 25, True, 12, False, [
                            "passport", "driver's license"])
    registry.register_voter("V002", "Jane Smith", 17,
                            True, 24, False, ["driver's license"])
    registry.register_voter("V003", "Bob Brown", 45,
                            False, 36, False, ["passport"])
    registry.register_voter("V004", "Alice Johnson", 30,
                            True, 3, False, ["passport"])
    registry.register_voter("V005", "Mike Wilson", 50,
                            True, 60, True, ["driver's license"])
    registry.register_voter("V006", "Sara Garcia", 22, True, 8, False, [])

    # Check eligibility of voters and handle exceptions
    voter_ids = ["V001", "V002", "V003", "V004", "V005", "V006", "V007"]

    for voter_id in voter_ids:
        print(f"\nChecking eligibility for voter ID: {voter_id}")
        try:
            registry.check_eligibility(voter_id)
            print(f"Voter {voter_id} is eligible to vote!")
        except AgeRequirementError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Wait until reaching voting age.")
        except CitizenshipError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Complete the naturalization process.")
        except RegistrationError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Register to vote at your local election office.")
        except ResidencyRequirementError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Wait until meeting residency requirements.")
        except FelonyConvictionError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Check state laws regarding restoration of voting rights.")
        except VoterIdError as e:
            print(f"Cannot vote: {e}")
            print("Solution: Obtain the required identification documents.")
        except VoterEligibilityError as e:
            print(f"Cannot vote: {e}")

    print("\n--- Example using can_vote method ---")
    for voter_id in ["V001", "V002", "V003"]:
        eligible, message = registry.can_vote(voter_id)
        status = "Eligible" if eligible else "Not eligible"
        print(f"Voter {voter_id}: {status} - {message}")


if __name__ == "__main__":
    main()
