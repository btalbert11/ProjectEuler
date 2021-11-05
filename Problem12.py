
def find_divisors(num):
    prime_factors = []
    factors_freq = []
    p = 0
    i = 2
    while i * i < num:
        if num % i == 0:
            prime_factors.append(i)
            factors_freq.append(0)
            while num % i == 0:
                factors_freq[-1] += 1
                num = num / i
        i = i + 1

    print(prime_factors)
    print(factors_freq)
    return sum(factors_freq) + 2

def main():
    tri_num = 3
    i = 2
##    while(find_divisors(tri_num) < 6):
        # find next triangle number
##        i += 1
##        tri_num = tri_num + i
    print(find_divisors(28))

if __name__ == "__main__":
    main()
