num = int(input("enter num"))
sum_val = sum(int(digit)**3 for digit in str(num))
print(f"{num} is Armstrong" if sum_val == num else "Not Armstrong")
