import re

input = map(
	lambda line : map(int, re.split(',|-', line)), 
	open("./input.txt")
)

def contains(a):
	return (a[0] >= a[2] and a[1] <= a[3]) or (a[0] <= a[2] and a[1] >= a[3])

def overlaps(a):
	return any(set(range(a[0], a[1] + 1)).intersection(range(a[2], a[3] + 1)))

print(sum(map(contains, input)))
print(sum(map(overlaps, input)))

