def find_letters_in_common(*args):
        # if we only have two strings, find all letters in common.
        if len(args) == 2:
                ret_val = ""
                for c in args[0]:
			# skip common characters we already know about
                        if c in ret_val:
                                continue

			# add any new common characters
                        if c in args[1]:
                                ret_val += c
		# return a string containing the unique common characters
                return ret_val

        # otherwise, recurse on the first argument and all remaining arguments.
        else:
                return find_letters_in_common(args[0], find_letters_in_common(*args[1:]))


def priority(letter):
	# 96 and 38 are the offsets between the ASCII values of these characters,
	# and the values we need for the puzzle.
	if letter.lower() == letter:
		return ord(letter) - 96
	if letter.upper() == letter:
		return ord(letter) - 38
	raise Exception()


part_1_priority = 0
part_2_priority = 0

first_rucksack = second_rucksack = third_rucksack = None

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()

		# part 1, calculate priority for each line.
		halfway = len(line) / 2
		first_compartment = line[0:halfway]
		second_compartment = line[halfway:]
		part_1_priority += priority(find_letters_in_common(first_compartment, second_compartment))

		# part 2, iterate over groups of three...
		if not first_rucksack:
			first_rucksack = line
		elif not second_rucksack:
			second_rucksack = line
		elif not third_rucksack:
			third_rucksack = line
			part_2_priority += priority(find_letters_in_common(first_rucksack, second_rucksack, third_rucksack))

			# ...then reset
			first_rucksack = second_rucksack = third_rucksack = None

print(part_1_priority)
print(part_2_priority)

