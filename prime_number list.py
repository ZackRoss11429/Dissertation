import math

number_searches = input("Input amount of numbers to be searched: ")
prime_list = []

for i in range(2, int(number_searches)):
    print(f"Checking if {i} is prime")
    isPrime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)
        print(f"{i} is prime!")

print(prime_list)

