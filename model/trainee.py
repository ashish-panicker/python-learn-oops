# Trainee class
class Trainee:
  # No class level variables
  def __init__(self, trainee_id: str, name: str, email: str):
      self._trainee_id = trainee_id
      self._name = name
      self._email = email

  @property
  def trainee_id(self):
      return self._trainee_id

  @trainee_id.setter
  def trainee_id(self, value):
      self._trainee_id = value

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, value):
      self._name = value