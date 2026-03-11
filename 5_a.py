def sum_of_primes(limit):
    sieve = [True] * limit 
    sieve[0] = sieve[1] = False
    for p in range(2 , int(limit ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p ,limit,p):
                sieve[i] = False

    prime_sum = sum(i for i , is_prime in enumerate(sieve) if is_prime)
    return prime_sum 

limit = 2000000
print(f"the sum of all primes below {limit} is {sum_of_primes(limit)}")