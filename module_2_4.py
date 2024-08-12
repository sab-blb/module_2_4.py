print(f"{"Задача"} {'"Всё не так уж просто"'}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers[0::]:
    for j in numbers[0::]:
        if i >= 2 and j >= 2:
            if i % j == 0 and i / j == 1:
                primes.append(i)
            elif i % j == 0 and i / j != 1:
                not_primes.append(i)
                break
print("Primes:", primes)
print("Not Primes:", not_primes)