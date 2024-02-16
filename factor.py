number = int(input("Insert a number"))
def factor(x):
    for i in range(1, x+1):
        if x % (i)==0:
            print(i)
            factor(number)