def fibonacci_generator(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

n = 10
fibonacci_numbers = fibonacci_generator(n)
print(fibonacci_numbers)
