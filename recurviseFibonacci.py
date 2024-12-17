print(0)
print(1)
count = 2

def recursiveFibonacci(fib1, fib2):
    global count
    if count <= 19:
        newFib = fib1 + fib2
        print(newFib)
        fib1 = fib2
        fib2 = newFib
        count += 1
        recursiveFibonacci(fib1, fib2)
    else:
        return
recursiveFibonacci(0, 1)