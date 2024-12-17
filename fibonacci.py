fib1 = 0
fib2 = 1
print(fib1, "\n", fib2)
for i in range(20):
    fib3 = fib1 + fib2
    print(fib3)
    fib1 = fib2
    fib2 = fib3