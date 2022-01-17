number = int(input("Please enter your number :"))

def factorial(number):
    a = 1
    b = False


    for i in range(number):
        a = a * (i+1)
        if a == number:
            print("Yeees")
            b = True
            break

    if b == False:
            print("Nooo")
            


factorial(number)