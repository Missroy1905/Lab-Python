def add(a,b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a // b

def calculator():
    while True: 
        print("1. add\n")
        print("2. sub\n")
        print("3. mul\n")
        print("4. div\n")
        print("5. exit\n")
        choice = int(input("enter choice:"))
        if choice == 5:
            break
        a = int(input("enter num 1 : "))
        b = int(input("enter num 2 : "))
        match(choice):
            case 1 :
                print("result:", add(a,b))
            case 2 :
                print("result:", sub(a,b))
            case 3 :
                print("result:", mul(a,b))
            case 4 :
                print("result:", div(a,b))


calculator()

