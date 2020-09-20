import math


def read_value(message,integer=False, positive=False, non_zero=False):
      input_number= input(message)
      try:
            number_value = float(input_number)
            if integer and not number_value.is_integer():
                  print("Value must be an integer")
                  number_value = read_value(message, integer, positive, non_zero)
            elif positive and number_value<0:
                  print("Value must be positive")
                  number_value= read_value(message, integer, positive, non_zero)
            elif non_zero and number_value==0:
                  print("Value must be non zero")
                  number_value = read_value(message, integer, positive, non_zero)
      except ValueError:
            print("Invialid Input. You must enter a number")
            number_value = read_value(message, integer, positive, non_zero)
      return number_value



def addition():
      first_value = read_value("Enter First number: ")
      second_value= read_value("Enter Second number: ")
      return first_value+second_value

def subtraction():
      first_value = read_value("Enter First number: ")
      second_value = read_value("Enter Second number: ")
      return first_value - second_value

def multiplication():
      first_value = read_value("Enter First number: ")
      second_value = read_value("Enter Second number: ")
      return first_value * second_value

def division():
      numerator = read_value("Enter Numerator: ")
      denominator = read_value("Enter Non Zero Denominator: ", non_zero=True)
      return numerator/denominator

def modulo():
      numerator = read_value("Enter Numerator: ")
      denominator = read_value("Enter Non Zero Denominator: ", non_zero=True)
      return numerator % denominator

def power():
      base_value = read_value("Enter base number: ")
      if base_value<0:
            power_value = read_value("Enter integer power number: ", integer=True)
      else:
            power_value = read_value("Enter power number: ")
      return math.pow(base_value, power_value)

def square_root():
      value = read_value("Enter non negative number: ", positive=True)
      return math.sqrt(value)

def logarithm():
      value = read_value("Enter non negative number: ", positive=True, non_zero=True)
      return math.log(value)

def exponential():
      value = read_value("Enter number: ")
      return math.exp(value)

def sine():
      angle_in_degrees = read_value("Enter angle in degrees: ")
      angle_in_radians = math.radians(angle_in_degrees)
      return math.sin(angle_in_radians)

def cosine():
      angle_in_degrees = read_value("Enter angle in degrees: ")
      angle_in_radians = math.radians(angle_in_degrees)
      return math.cos(angle_in_radians)

def tangent():
      angle_in_degrees = read_value("Enter angle in degrees: ")
      angle_in_radians = math.radians(angle_in_degrees)
      return math.tan(angle_in_radians)
