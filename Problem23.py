import math
cap = 28124 # not including

def divisor_sum(num):
    dsum = 0
    for i in range(1, 1 + math.ceil(num/2)):
        if num % i == 0:
            dsum += i
    return dsum


def find_abundant_nums():
    anums = []
    # find all abundant nums
    for i in range(1, cap):
        if i < divisor_sum(i):
            anums.append(i)
    return anums


def find_sum(anums):
    nums = [] # all numbers than cannot be written as sum of 2 anums
    for i in range(1, cap):
        is_sum = False
        for j in anums:
            if j >= i:
                break
            # if i - j is in anums, then i is sum of 2 anums
            if (i - j) in anums:
                is_sum = True
                break
        if not is_sum:
            nums.append(i)
    return sum(nums)

def main():
    #generate abundant numbers
    anums = find_abundant_nums()
    print(find_sum(anums))



if __name__ == "__main__":
    main()
