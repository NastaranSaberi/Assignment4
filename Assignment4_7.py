number1 = int(input("Please enter first number :"))
number2 = int(input("Please enter second number :"))

def gcd (number1 , number2):

    if number1 == number2:
        kmm = number1

    if number1 > number2:
        kmm = number1

    elif number2 > number1 :
        kmm = number2
        
    while kmm > 1 :
        if kmm % number1 == 0 and kmm % number2 == 0 :
            print(kmm)
            break
        
        else:

            kmm +=1
            if kmm % number1 == 0 and kmm % number2 == 0 :
                print(kmm)
                break


gcd (number1 , number2)
