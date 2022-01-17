number1 = int(input("Please enter first number :"))
number2 = int(input("Please enter second number :"))

def gcd (number1 , number2):

    if number1 == 0:
        print("Please enter a natural number !!!")

    elif number2 == 0:
        print("Please enter a natural number !!!")

    if number1 == number2:
        bmm = number1

    if number1 > number2:
        bmm = number2

    elif number2 > number1 :
        bmm = number1
        
    while bmm > 1 :
        if number1 % bmm == 0 and number2 % bmm == 0 :
            print(bmm)
            break
        
        else:

            bmm -=1
            if number1 % bmm == 0 and number2 % bmm == 0 :
                print(bmm)
                break


gcd (number1 , number2)

