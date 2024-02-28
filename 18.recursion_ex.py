def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

print(f"Factorial of 4 is {fact(5)}")