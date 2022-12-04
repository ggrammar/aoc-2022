import re

def input_to_two_ranges(input):
	a, b, c, d = map(int, re.split(',|-', input))
	return range(a, b + 1), range(c, d + 1)

def contains(first, second):
	if (len(first) == 1) and (first in second):
		return True

	if first[0] >= second[0]:
		if first[-1] <= second[-1]:
			return True

	return False

def bidirectional_contains_on_two_ranges(ranges):
	return contains(ranges[0], ranges[1]) or contains(ranges[1], ranges[0])

def overlaps_on_two_ranges(ranges):
	# only set has the 'intersection' method, but it accepts any iterable as an argument.
	return any(set(ranges[0]).intersection(ranges[1]))

with open("./input.txt", "r") as f:
	ranges = map(input_to_two_ranges, f.readlines())

print("Part 1 :: {}".format(sum(map(bidirectional_contains_on_two_ranges, ranges))))
print("Part 2 :: {}".format(sum(map(overlaps_on_two_ranges, ranges))))

