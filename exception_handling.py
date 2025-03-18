"""
Exception - conditions or events that occur in the program that affects the normal executiuon of the program.
We have to handle exceptions to ensure the normal execution of the program.

Handle exceptions
1. try-except
2. try-expect-else
3. try-except-finally
4. try-except-else-finally
"""
num1 = 0
num2 = 0
try:    # Encloses statements that can cause exceptions
  # Accept the input from the user and convert it to int
  num1 = int(input("Enter number 1: ")) 
  num2 = int(input("Enter number 2: ")) # throws ValueError 
  result = num1/ num2
except ZeroDivisionError:
  print(f"Division by zero not allowed: {num2} ")
except ValueError:
  print(f"Please provide numbers.")
else:     # Only works incase there is no exception
  print(f"Result = {result}")
finally:  # Always works irrespective of exceptions.
  print("Program execution complete!")