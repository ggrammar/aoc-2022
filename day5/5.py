with open("./input.txt")  as  f:
	input = f.readlines()

crate_lines = []
instructions = []
num_crates = 0

reading_crates = True

for line in input:
	line = line.replace("\n", "") # preserve whitespace, but not newlines

	if not line:
		print("finished reading crate data, reading instructions now.")
		reading_crates = False

	if reading_crates:
		if "1" in line:
			num_crates = (int(max(line.split(" "))))
		else:
			crate_lines += line

	else:
		instructions.append(line)


class column_of_crates:
	def __init__(self, crates):
		self.crates = crates

	def add_crate(self, crate):
		for i in range(0, len(self.crates)):
			if not self.crates[i]:
				self.crates[i] = crate
				return
		self.crates.append(crate)

	def add_crate_to_bottom(self, crate):
		self.crates.insert(0, crate)

	def remove_crate(self):
		return self.crates.pop()

all_crates = []
for c in range(0, num_crates):
	all_crates.append(column_of_crates([]))

length_of_each_line = num_crates * 4 - 1

# starting at the top row of crates, work our way down
for i in range(0, len(crate_lines), length_of_each_line):
	row_of_crates = (crate_lines[i:length_of_each_line + i])
	print(row_of_crates)

	# iterate 4 characters at a time to see each column
	for crate_start in range(0,  len(row_of_crates), 4):
		column_number = crate_start / 4
		crate_letter = row_of_crates[crate_start:crate_start + 3][1]

		if crate_letter != ' ':
			all_crates[column_number].add_crate_to_bottom(crate_letter)

def print_all_crates(cs):
	for column in cs:
		line = ""
		for crate in column.crates:
			if not crate:
				line += "    "
			else:
				line += "[{}] ".format(crate)
		print(line)

print("--- start ---")
print_all_crates(all_crates)

for i in instructions:
	if not i:
		continue

	print("--- {} ---".format(i))

	tmp, count, tmp, from_col, tmp, to_col = i.split(" ")

	count = int(count)
	from_col = int(from_col) - 1
	to_col = int(to_col) - 1

	ordered_crates = ""
	for c in range(0, count):
		# part 1
		# all_crates[to_col].add_crate(all_crates[from_col].remove_crate())

		# part 2
		ordered_crates += all_crates[from_col].remove_crate()
	ordered_crates = ordered_crates[::-1]

	for c in ordered_crates:
		all_crates[to_col].add_crate(c)
		

	print_all_crates(all_crates)
	

print("--- end ---")
