import re

def input_to_two_ranges(input):
	a, b, c, d = re.split(',|-', input)
	return range(int(a), int(b) + 1), range(int(c), int(d) + 1)

def directional_contains(first, second):
	if (len(first) == 1) and (first in second):
		return True

	if first[0] >= second[0]:
		if first[-1] <= second[-1]:
			return True

def bidirectional_contains_on_two_ranges(ranges):
	if directional_contains(ranges[0], ranges[1]) or directional_contains(ranges[1], ranges[0]):
		return 1
	return 0

def overlaps_on_two_ranges(ranges):
	for i in ranges[0]:
		if i in ranges[1]:
			return 1
	return 0

with open("./input.txt", "r") as f:
	ranges = map(input_to_two_ranges, f.readlines())

print("Part 1 :: {}".format(sum(map(bidirectional_contains_on_two_ranges, ranges))))
print("Part 2 :: {}".format(sum(map(overlaps_on_two_ranges, ranges))))

