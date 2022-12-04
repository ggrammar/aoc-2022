import re

input = map(
	lambda line : map(int, re.split(',|-', line)), 	
	open("./input.txt")
)

contains = lambda a : (
	a[0] >= a[2] and a[1] <= a[3]
	or a[0] <= a[2] and a[1] >= a[3]
)

overlaps = lambda a : any(set(range(a[0], a[1] + 1)).intersection(range(a[2], a[3] + 1)))

print("{}, {}".format(sum(map(contains, input)), sum(map(overlaps, input))))

