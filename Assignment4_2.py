import math

def Quadratic_equation(a,b,c):

    if (b**2) - (4*a*c) == 0:
        x = -b / 2*a
        print("Answer:",x)

    elif (b**2) - (4*a*c) > 0 :
        print("x1:" ,(-(b) + math.sqrt((b**2)-(4*a*c)))/(2*a))
        print("x2:" ,(-(b) - math.sqrt((b**2)-(4*a*c)))/(2*a))

    elif (b**2) - (4*a*c) < 0:
        print("the equation has no answer")

    



a = float(input("Quadratic_equation :  ax^2 + bx + c = 0 \n enter a :"))
b = float(input("Quadratic_equation :  ax^2 + bx + c = 0 \n enter b :"))
c = float(input("Quadratic_equation :  ax^2 + bx + c = 0 \n enter c :"))

Quadratic_equation(a,b,c)