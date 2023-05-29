import sys
import csv

def calc(names):
	s = 0
	i = 1
	for name in names:
		char_sum = 0
		for c in name:
			char_sum += ord(c) - 64
		char_sum *= i
		s += char_sum
		i += 1
	return s


def main(f):
	f_reader = csv.reader(f, delimiter=',')
	names = list(f_reader)[0]
	names.sort()		
	s = calc(names)
	print(s)


if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	main(f)
