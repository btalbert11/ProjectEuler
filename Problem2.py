import string

def main():
    termp = 1
    term = 2
    sum = 0
    while term < 4000000:
        if term % 2 == 0:
            sum = sum + term
        print(sum, term, termp)
        newterm = term + termp
        termp = term
        term = newterm

    print(sum)

if __name__ == "__main__":
    main()
