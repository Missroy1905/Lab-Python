def sum_even_fibonacci(limit):
    a , b = 1 , 2 
    total_sum = 0 
    while a<= limit:
        if a % 2 ==0 :
            total_sum += a 
        
        a ,b = b , a +b 

    return total_sum 

limit = 4000000
print(f"the sum of even fibonacci terms upto{limit} is {sum_even_fibonacci(limit)}")
