


def main():
    i = 2
    num = 600851475143
    while i * i < num:
        if num % i:
            i += 1
        else:
            num = num / i
        print(i)
    print(num)



if __name__ == "__main__":
    main()
