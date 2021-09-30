def check_div(num):
    if (num % 20) or (num % 19) or (num % 18) or (num % 17) \
    or (num % 16) or (num % 15) or (num % 14) or (num % 13) \
    or (num % 12) or (num % 11):
        return False
    return True

def main():
    answer = 21
    while not check_div(answer):
        answer += 1
##        if not (answer % 100000):
##            print(answer)
    print(answer)

if __name__ == "__main__":
    main()
