def fibonacci_buzzfizz(n):
    # start with 1 and manually yield Buzz for 0 % 3 == 0
    a, b, count = 2, 3, 2
    multiples = set()
    result = ['Buzz', 1]

    #get upper bound for prime sieve
    varphi = (1 + 5 ** 0.5 ) / 2.0
    phi = (1 - 5 ** 0.5) / 2.0
    max_fib = int((varphi ** n - phi ** n) / float(varphi - phi))

    while count < n:
        if a not in multiples:
            result.append('BuzzFizz')
        elif a % 3 == 0:
            result.append('Buzz')
        elif a % 5 == 0:
            result.append('Fizz')
        else:
            result.append(a)
        # sieve for primes
        for c in range(a, b + 1, 1):
            multiples.update(range(c * c, max_fib + 1, c))
        a, b = b, a + b
        count += 1
    return result

