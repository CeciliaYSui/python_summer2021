import keyword
# print(keyword.kwlist)

# List of exceptions:
#  - raise: 
#       to create exceptions or errors
#  - pass 
#       to continue execution without doing anything
#  - try: 
#       tries executing the following
#  - except TypeError: 
#       runs if a Type Error was raised
#  - except: 
#       runs for all types of errors or exceptions; be careful
#  - else:  
#       runs if there was no exception/error
#  - finally: 
#       always runs


for n in range(2, 10):
    for x in range(2, n): 
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')