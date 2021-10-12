
def main():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1000):
                # is pyth triplet
                if (a < b and a < c and b < c) and (a + b + c == 1000) and (a**2 + b**2 == c**2):
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
