import sys
import csv

def main(f):
	f_reader = csv.reader(f, delimiter=',')
	names = list(f_reader)[0]
	names.sort()		
	print(names)


if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	main(f)
