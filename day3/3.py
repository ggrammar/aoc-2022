def find_letters_in_common(*args):
        # If we only have two strings, find all letters in common.
        if len(args) == 2:
                ret_val = ""
                for c in args[0]:
                        if c in ret_val:
                                continue

                        if c in args[1]:
                                ret_val += c
                return ret_val
        # Otherwise, recurse on the first argument and all remaining arguments.
        else:
                return find_letters_in_common(args[0], find_letters_in_common(*args[1:]))


def priority(letter):
	if letter.lower() == letter:
		return ord(letter) - 96
	if letter.upper() == letter:
		return ord(letter) - 38
	raise Exception()


part_1_priority = 0
part_2_priority = 0
first = second = third = None

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()

		# part 1, calculate priority for each line.
		halfway = len(line) / 2
		first_compartment = line[0:halfway]
		second_compartment = line[halfway:]
		part_1_priority += priority(find_letters_in_common(first_compartment, second_compartment))
		

		# part 2, iterate over groups of three...
		if not first:
			first = line
		elif not second:
			second = line
		elif not third:
			third = line
			part_2_priority += priority(find_letters_in_common(first, second, third))

			# ...then reset
			first = second = third = None

print(part_1_priority)
print(part_2_priority)

