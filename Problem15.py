import numpy as np
import math
def lat(n):
    denom = math.factorial(n)
    count = math.factorial(2*n) / (denom * denom)
    return count



def main():
    
    n = 20
    print(lat(n))



if __name__ == "__main__":
    main()
