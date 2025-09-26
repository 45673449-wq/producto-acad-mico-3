def fibonacci(n):
    if n <= 0:
        raise ValueError("n debe ser un número positivo")
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
