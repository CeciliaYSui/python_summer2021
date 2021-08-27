## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if y > x: 
        a,b = y,x
    else: 
        a,b = x,y
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

# testing
# print(gcd(270, 192))
# print(gcd(5,192))


## Problem 2
## Write a function using recursion that returns prime numbers less than 121
## remember, primes are not the product of 
## any two numbers except 1 and the number itself
## hint, "hardcode" 2
import math
from typing import Tuple
# sol for 10: 2, 3, 5, 7
def find_primes(me = 121, primes = []):
    # hardcode 2
    # Base case: 
    if me == 2: 
        primes.append(2)
        return primes

    # when me > 2
    # Recursive case: 
    flag = True
    for i in range(2, math.floor(math.sqrt(me))+1):
        if me % i == 0: 
            flag = False # not a prime 
            break
    if flag: 
        primes.append(me) # append the prime
    # recursion
    return find_primes(me-1, primes)

# testing
# print(find_primes())

 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

# 

def T(n, from_rod, to_rod, mid_rod):
    # Base case: n = 1
    if n == 1: 
        print("Move 1 disk from {} to {}".format(from_rod, to_rod))
    # Recursive case: n > 1
    # call T() again 
    else: # n > 2
        T(n-1, from_rod, mid_rod, to_rod)
        print("Move {} disk from {} to {}".format(n, from_rod, to_rod))
        T(n-1, mid_rod, to_rod, from_rod)
# testing 
T(4, "A", "C", "B")
