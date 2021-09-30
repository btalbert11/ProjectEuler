

def main():
    sum = 0
    square = 0
    for i in range(100):
        square += (i + 1)
        sum = sum + ((i + 1) ** 2)
    square = square ** 2
    print(square, sum, square - sum)
if __name__ == "__main__":
    main()
