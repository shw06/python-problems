def fact(n):
    if n == 0:
        print("Invalid number")
    if n == 1 or n == 2:
        return 1
    else:
        print(n * fact(n-1))

n = 5
print("factorial is",fact(n))

for i in range(0,n):
    print(fact(n))
