def fib(max):
    odd, even = 0, 1
    while odd < max:
        yield odd
        odd, even = even, odd + even

print(sum(filter(lambda n: n % 2 == 0, fib(4000000))))