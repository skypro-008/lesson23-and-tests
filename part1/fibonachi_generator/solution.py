def fib(n):
    index = 0
    prev = 0
    current = 1
    while index < n:
        yield prev
        prev, current = current, prev + current
        index += 1


fib_gen = fib(15)

if __name__ == "__main__":
    print(list(fib_gen))
