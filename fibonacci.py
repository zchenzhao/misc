from math import sqrt

def fibonacci(n):
    if type(n) != int or n < 1:
        # index in Fibonacci sequence must be an integer of value 1 or greater
        print('Invalid input.')
        return
    else:
        # Binet's formula
        phi = (sqrt(5) + 1) / 2
        answer = (phi**n - (-phi)**(-n)) / sqrt(5)

        return int(round(answer))
