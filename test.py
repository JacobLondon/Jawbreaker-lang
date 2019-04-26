def fib(n):
    if n <= 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)



def main():
    n = 10
    out = fib(n)
    print(out)

main()