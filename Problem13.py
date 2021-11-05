

def main():
    num_str = []
    with open('input_problem13.txt') as f:
        num_str = f.readlines()

    sum = 0
    for i in num_str:
        sum += int(i)
    print(sum)
if __name__ == "__main__":
    main()
