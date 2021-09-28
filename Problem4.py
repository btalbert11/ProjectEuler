

def is_palindrome(num):
    chk = str(num)
    l = len(chk)
    for i in range(int(l / 2)):
        if (chk[i] != chk[l - 1 - i]):
                return False
    return True


def main():
    max_num = 999
    largest_pal = 0

    for i in range(1, max_num + 1):
        for j in range(i, max_num + 1):
            chk = i * j
            if is_palindrome(chk) and (chk) > largest_pal:
                largest_pal = chk
    print(largest_pal)

if __name__ == "__main__":
    main()
