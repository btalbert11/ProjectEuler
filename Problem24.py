## What is the millionth lexicographic permutation of th digits {0,1,2,3,4,5,6,7,8,9}
## The "WHAT IS THIS WORD CALLED" solution is list out permutations, sort, and print millionth.
## instead of listing them out, you would just manipulate the array in lexicographic order until you hit the millionth

## Recursive solution, base case swap digits, non base swap head with next integer, do until you recurse with all intsi

def swap_pos(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    
# find the smallest int that is greater than head_pos
def flip_head(perm_list, head_pos):
    curr = len(perm_list)
    new_head_pos = -1
    for i in range(head_pos + 1, len(perm_list)):
        if perm_list[i] > perm_list[head_pos] and perm_list[i] < curr:
            new_head_pos = i
            curr = perm_list[i]
    swap_pos(perm_list, head_pos, new_head_pos)

# reverse the list after the head position
def reverse_tail(perm_list, head_pos):
    start = head_pos + 1
    end = len(perm_list) - 1
    while start < end:
        swap_pos(perm_list, start, end)
        start += 1
        end -= 1

def greater_than_tail(perm_list, head_pos):
    for i in range(head_pos + 1, len(perm_list)):
        if perm_list[head_pos] < perm_list[i]:
            return False
    return True

def find_perms(perm_list, head_pos, count):
    
    # Base case, head_pos = len-2, swap last two elements. 
    # end_pos is 8 for this problem
    end_pos = len(perm_list) - 2
    if head_pos == end_pos:
        swap_pos(perm_list, end_pos, end_pos+1)
        #print(perm_list)
        #breakpoint()
        return count + 1

    # non base case, flip head_pos with next integer, reverse list after head, do until head_pos is greater than the rest of the list, recurse each time
    while(not greater_than_tail(perm_list, head_pos)):
        # recurse to find permutations for tail of list
        count = find_perms(perm_list, head_pos + 1, count)
        if count == 1_000_000:
            print(perm_list)
            exit()
        # flip head and next int
        flip_head(perm_list, head_pos)
        reverse_tail(perm_list, head_pos)
        count += 1
        if count == 1_000_000:
            print(perm_list)
            exit()
        #breakpoint()
        #print(perm_list)

    # Need to count permutations for the final head position, which is now 9
    count = find_perms(perm_list, head_pos + 1, count)
    if count == 1_000_000:
        print(perm_list)
        exit()
    #print(perm_list)
    #breakpoint()
    return count




    

def main():
    perm = [0,1,2,3,4,5,6,7,8,9]
    count = 1
    

    print(perm)
    print(greater_than_tail([0,2,1,3], 1))
    breakpoint()
    count = find_perms(perm, 0, count)
    print(count)



if __name__ == "__main__":
    main()


## Idea!
## make it recursive, each subset you are sortin the order, and then swaping the outside number with the next highest number
#perms

0,1,2,3,4
0,1,2,4,3
0,1,3,2,4
0,1,3,4,2
0,1,4,2,3
0,1,4,3,2
0,2,1,3,4
0,2,1,4,3
0,2,3,1,4
0,2,3,4,1
0,2,4,1,3
0,2,4,3,1
0,3,1,2,4
0,3,1,4,2
0,3,2,1,4
0,3,2,4,1
0,3,4,1,2
0,3,4,2,1


1,0,2,3,4
1,0,2,4,3
1,0,3,2,4
1,0,3,4,2
1,0,4,2,3
1,0,4,3,2
#    1,0,4,3,2
#    1,2,4,3,0
#    1,2,0,3,4
1,2,0,3,4



0,1,4,2,3
0,1,4,3,2
0,1,

