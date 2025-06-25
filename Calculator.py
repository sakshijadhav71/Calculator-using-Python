
#***************************************************************CALCULATOR *****************************************************************


def add(number1, number2):
    return number1 + number2 

def sub(number1, number2):
    return number1 - number2

def multiply(number1, number2 ):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def avg(number1,number2):
    return (number1 + number2)

print("Select a opertion:\n"\
      "1. Addition\n"\
      "2. Substraction\n"\
      "3. Mumltiplication\n"\
      "4.Division\n"\
      "5. Average\n")

inst=int(input("Select operation from 1,2,3,4,5:"))

num1= int(input("Enter a first number: "))
num2=  int(input("Enter a second number: "))

if inst==1:
    print(num1, "+", num2, "=", \
          add(num1, num2))
    
elif inst==2:
    print(num1, "-", num2, "=", \
          sub(num1, num2))    
    
elif inst==3:
    print(num1, "X", num2, "=", \
          multiply(num1, num2))
    
elif inst==4:
    print(num1, "/", num2, "=", \
          division(num1, num2))    

elif inst==5:
    print(num1, "+", num2, "=", \
          avg(num1, num2))    
    
else:
    print("invalid operation! Pls select again!")    