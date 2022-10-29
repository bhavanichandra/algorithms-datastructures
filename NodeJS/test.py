from math import ceil


def check(n):
    square_sum = 0
    while n > 0:
        reminder = n % 10
        
        n = n / 10
    while square_sum > 1:
        square_sum = check(square_sum)    


print(check(31))