# Create a mock Database connection class and simulate raising a predefined exception
import random
class Database:
  """Dummy Database connection class"""
  def connect(self, credentials):
    self.credentials = credentials
    if random.choice([True, False]): # Simulating a Timeout
      # TimeoutError is predefined by python
      raise TimeoutError("Connection taking too much time.")
    print(f"Connection open.")

  def close(self):
    print(f"Connection closed.")

db = Database()
try:
  db.connect("") # Could possibly raise exceptions
except TimeoutError:
  print("Connection timeout")
finally:
  db.close()