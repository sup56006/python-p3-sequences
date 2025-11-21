def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fib = [0]

    if length > 1:
        fib.append(1)

    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib)
