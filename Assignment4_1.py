m = int(input("Number of objects in length:"))
n = int(input("Number of objects in width:"))

def dimensions(m,n):
    
    for i in range(m):

        if i % 2 !=0: 
            for i in range(n):
                if i % 2 != 0:
                    print("*", end="")
                elif i % 2 == 0:
                    print("#", end="")


        if i % 2 == 0:
            for i in range(n):
                if i % 2 != 0:
                    print("#", end="")
                elif i % 2 == 0:
                    print("*", end="")   

        print()

dimensions(m,n)


    