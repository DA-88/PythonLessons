n = input("Введите N: ")

print(max(list(n)))

n = int(n)
max_digit = int(0)
while n > 0:
    max_digit = max(max_digit, n % 10)
    n = n // 10

print(max_digit)