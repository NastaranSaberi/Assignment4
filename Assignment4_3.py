n = int(input("Enter the number of vertical columns :"))
m = int(input("Enter the number of horizontal columns :"))


def Multiplication_table (n , m):

    for i in range (1 , n+1):
        
        for j in range (1 , m+1):
            print(i*j , end= "\t")


        print("\n")


Multiplication_table(n , m)
