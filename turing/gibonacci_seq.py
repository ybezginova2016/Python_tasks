def solution(n: int, x: int, y: int):
    if n in (0, 1):
        return 0
    previous, fib_number = x, y
    for _ in range(1, n):
        previous, fib_number = fib_number, fib_number - previous
    return fib_number

print(solution(2, 0, 1))