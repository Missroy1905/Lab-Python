a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

def gcd(a,b):
    while b:
        a, b = b, a%b
    print(a) 

print("the GCD of" , a , "and" , b ,"is", gcd(a,b))
 
    
