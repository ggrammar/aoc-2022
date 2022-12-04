def input_to_range(input):
	first, second = input.split("-")
	return range(int(first), int(second) + 1)


def contains(first, second):
	if len(first) == 1:
		if first in second:
			return True

	if first[0] >= second[0]:
		if first[-1] <= second[-1]:
			return True

	return False


def overlaps(first, second):
	for i in first:
		if i in second:
			return True
	

contains_total = 0
overlaps_total = 0

with open("./input.txt", "r") as f:
	for line in f.readlines():
		print(line)

		# first and second are a range of one or more consecutive integers
		first = input_to_range(line.split(",")[0])
		second = input_to_range(line.split(",")[1])

		print(first)
		print(second)

		if (
			contains(first, second)
			or contains(second, first)
		):
			contains_total += 1

		if (
			overlaps(first, second)
			or overlaps(second, first)
		):
			overlaps_total += 1

print("{}, {}".format(contains_total, overlaps_total))

