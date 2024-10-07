import math 
try: 
  def add(a, b):
    return a + b
  def subtract(a, b):
    return a - b
  def multiply(a, b):
    return a * b
  def divide(a, b):
    return a / b
  a = float(input('Would you kindly input a number. '))
  b = float(input('Would you kindly input a number. '))
  operator = input('Would you kindly pick a operator, which could be +, -, / or *. ')
  if operator == '+':
    result = add(a, b)
  elif operator == '-':
    result = subtract(a, b)
  elif operator == '*':
    result = multiply(a, b)
  elif operator == '/':
    result = divide(a, b)
  else:
    print('You have entered a value that is not a symbol so the calcltor has stopped.')
    exit()
  print('This is your answer:', result)
except ZeroDivisionError:
  print('You cannot divde by zero.')
except ValueError:
  print('You have entered a invaild data type.')
finally:
  print('The code is complete its run.')
      
