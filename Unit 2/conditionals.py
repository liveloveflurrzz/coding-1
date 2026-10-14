# Conditional if/else logic- these are keywords that instruct your 
# program to do specific instructions based on specific data 
# or conditions


# condititional syntax (how it is written)
   
# if usually indicates that something is a possible option
   
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
  
# else is ALWAYS your last option. 
    






def calculate_add():
    print("Program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    print("Program has ended.")


def calculate_subtract():
    print("Program has started: please type in 2 numbers to subtract ")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print("Program has ended.")

def calculate_multiply():
    print("Program has started: please type in 2 numbers to multiply ")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
    print("Program has ended.")

def calculate_division():
    print("Program has started: please type in 2 numbers to divide ")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
    print("Program has ended.")


def mainCalculator():
    print("main calculator is running... ")
    selection = int(input())
     if selection == 1:
     calculate_add()
    elif selection == 2:
     calculate_subtract()
     elif selection == 3:
      calculate_multiply()
      elif selection == 4:
      calculate_divide()
      else:
    print("sorry i dont understand your selection")

        mainCalculator()    
