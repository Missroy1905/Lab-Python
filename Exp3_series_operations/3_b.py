n = int(input("enter num"))

def fib_series(n, a = 0, b = 1):
    
    if n > 0 :
        if n > 1:
            print(a, end =", ")
        else:
            print(a)

        fib_series(n-1, b, a+b)

fib_series(n)
