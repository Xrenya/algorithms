n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return 1/n + factorial(n-1)
        
factorial(n)
