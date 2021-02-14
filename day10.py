##calculator

#Add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-": subtract,
  "*": multiply,
  "/": divide
  }
def calculator ():
  num1= float(input("What is the first number?: \n"))
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: \n")
    num2= float(input("What is the next number?: \n"))
    calculation_function = operations[operation_symbol]
    answer=calculation_function(num1,num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    continue_with = input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation \n")

    if continue_with == 'y':
      should_continue
      num1=answer
    else:
      should_continue = False
      calculator()

calculator()