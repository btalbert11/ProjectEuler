import sys

def find_max(rows, curr_row, curr_index, curr_sum):
    
    curr_sum = curr_sum + rows[curr_row][curr_index]
    curr_row += 1
    # ending condition, last row
    if (curr_row >= len(rows)):
        return curr_sum

    p1 = find_max(rows, curr_row, curr_index, curr_sum)

    p2 = find_max(rows, curr_row, curr_index + 1, curr_sum)
    
    return p1 if p1>=p2 else p2


def main():
    lines = []

    with open(sys.argv[1]) as file:
        lines = file.readlines()
    print(lines)
    for l in lines:
        print(l.rstrip())
    rows = []
    for l in lines:
        rows.append([int(x) for x in l.rstrip().split()])
    print(rows)
    

    print(find_max(rows, 0, 0, 0))


if __name__ == "__main__":
    main()
