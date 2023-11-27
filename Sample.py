import math

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

#Operation = int(input("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulo \n6. Raise to a power"))
Operation = int(input('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulo
6. Raise to a power
'''))

if Operation == 1:
    Addition = num1 + num2
    print("the Addition of Number is: ",Addition)
elif Operation == 2:
    Subtraction = num1 - num2
    print("the Subtraction of Number is: ",Subtraction)
elif Operation == 3:
    Multiplication = num1 * num2
    print("the Multiplication of Number is: ",Multiplication)
elif Operation == 4:
    if num2 != 0:
        Divison = num1 / num2
        print("the Divison of Number is: ",Divison)
    else:
        print("Divison not Possible")
elif Operation == 5:
    if num2 != 0:
        Modulo = num1 % num2
        print("the Modulo of Number is: ",Modulo)
    else:
        print("Modulues not Possible")    
elif Operation == 6:
    Raise=math.pow(num1,num2)
    print("the Raise to a power of Number is: ",Raise)
else:
    print("select Proper Option")
    
