
def generate_primes(n):
    primes = [True] * (n+1)
    i = 2
    while i**2 <= n:
        # current one is prime, not marked yet
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1
    set_primes = []
    for i in range(2, n+1, 1):
        if primes[i]:
            set_primes.append(i)
    return set_primes

def main():
    primes = generate_primes(10)
    print(primes, sum(primes))

if __name__ == "__main__":
    main()
