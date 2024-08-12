print(f"{"Задача"} {'"Всё не так уж просто"'}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i, j in enumerate(numbers):
    if j < 2:
        continue
    is_prime = True
    for div in range(2, j):
        if j % div == 0:
            not_primes.append(j)
            is_prime = False
            break
    if is_prime:
        primes.append(j)
print("Primes:", primes)
print("Not Primes:", not_primes)