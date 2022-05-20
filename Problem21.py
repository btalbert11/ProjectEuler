
# initalize an array of 10,000 to all 0, each index is for (# - 1)
# index = number - 1, number = index + 1
# compute sum of all number's proper divisors
# run through list, if a pair is found mark each as -1 to show they are
#     now paired up
# keep running sum


def compute_divisor_sum(num):
    sum = 0
    for i in range(1, (num//2) + 1):
        if num % i == 0:
            sum += i
    return sum


def main():
    max_num = 10000
    nums = [0] * max_num
    # compute all of divisor sums
    for i in range(max_num):
        nums[i] = compute_divisor_sum(i + 1)
        print(nums[i])
    
    sum = 0
    # find divisor sum pairs, compute sum
    for i in range(1, max_num):
        other_num = nums[i] - 1
        if nums[i] != -1 and nums[i] <= 10000 and nums[i] != i + 1 and nums[other_num] == i + 1:
            print(i + 1, nums[i], other_num, nums[other_num])
            sum += nums[i]
            sum += i + 1
            nums[nums[i] - 1] = -1
            nums[i] = -1

    print(sum)

if __name__ == "__main__":
    main()
