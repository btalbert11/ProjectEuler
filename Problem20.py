

def find_fact(n):
    prod = 1
    while n >= 1:
        prod = prod * n
        n = n - 1
    return prod

def main():

    digit_sum = 0
    num = find_fact(100)
    while num > 0:
        digit_sum += num % 10
        num = num // 10
    print(digit_sum)

if __name__ == "__main__":
    main()
