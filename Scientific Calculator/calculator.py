import calculatorBase
operations = {
      0: "Addition",
      1: "Subtraction",
      2: "Multiplication",
      3: "Division",
      4: "Modulo",
      5: "Power",
      6: "Square Root",
      7: "Logarithm",
      8: "Exponential",
      9: "Sine",
      10: "Cosine",
      11: "Tangent",
}


def showMenu():
    return """Choose an option from the menu:\n
0- Addition
1- Subtraction
2- Multiplication
3- Division
4- Modulo
5- Power
6- Square Root
7- Logarithm
8- Exponential
9- Sine
10- Cosine
11- Tangent

Your option from the menu: """

def read_input(operations):
      user_input = input(showMenu())
      try:
            valid_input = int(user_input)
            while valid_input not in operations.keys():
                  print("\nInvalid Input\n")
                  valid_input= read_input(operations)
      except:
            print("\nInvalid Input\n")
            valid_input =read_input(switcher)
      return valid_input

while True:
      input_value = read_input(operations)

      if input_value==0:
            result = calculatorBase.addition()
      elif input_value == 1:
            result = calculatorBase.subtraction()
      elif input_value == 2:
            result = calculatorBase.multiplication()
      elif input_value == 3:
            result = calculatorBase.division()
      elif input_value == 4:
            result = calculatorBase.modulo()
      elif input_value == 5:
            result = calculatorBase.power()
      elif input_value == 6:
            result = calculatorBase.square_root()
      elif input_value == 7:
            result = calculatorBase.logarithm()
      elif input_value == 8:
            result = calculatorBase.exponential()
      elif input_value == 9:
            result = calculatorBase.sine()
      elif input_value == 10:
            result = calculatorBase.cosine()
      elif input_value == 11:
            result = calculatorBase.tangent()

      print("Result: ", result)
      repeat = input("\nPerform another operation? (y) ")
      if repeat.lower() !='y':
            break
      print("\n")
