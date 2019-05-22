def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a


def fibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        a = (fibonacciRecursion(n-1) + fibonacciRecursion(n-2))
        return a
        

if __name__ == "__main__":
    c = int(input("Enter Numbers of Fibonacci Sequence:"))
    for i in range(c):
        print(fibonacci(i))
        print(fibonacciRecursion(i))




