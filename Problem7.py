
def main():
    primes = [2]
    i = 3
    prime = True
    while len(primes) != 10001:
        for num in primes:
            if i % num == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        prime = True
        i += 2
    print(primes[-1])


if __name__ == "__main__":
    main()
