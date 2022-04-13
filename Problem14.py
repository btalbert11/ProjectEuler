
#def coltz_length(i):
#    if i == 1:
#        return 1
#    elif (i % 2) != 0: # is odd
#        return coltz_length((3 * i) + 1) + 1
#    else: # is even
#        return coltz_length(i / 2) + 1

def coltz_length(i):
    length = 0
    while (i != 1):
        if (i % 2) != 0: # is odd
            length += 1
            i = (3 * i) + 1
        else: # is even
            length += 1
            i = (i / 2)
    return length + 1
    

def main():
    max_len = 1
    max_i = 1
    for i in range(1, 1000001):
        length = coltz_length(i)
        if length > max_len:
            max_len = length
            max_i = i
    print(max_len)
    print(max_i)

if __name__ == "__main__":
    main()