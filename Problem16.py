


def main():
    n = 1000
    pow_sum = 0
    power = 2**n
    pow_str = str(power)
    for i in pow_str:
        pow_sum += int(i)
    print(pow_sum)
    pow_sum = 0
    for i in range(len(str(power))):
        digit = power % 10
        pow_sum += digit
        power = int(power // 10)
    print(pow_sum)


if __name__ == "__main__":
    main()
    test = 2**100
    print(test)
    print(test // 10)
    print(int(test // 10))
