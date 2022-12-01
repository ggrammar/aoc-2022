elf = 0
biggest_elf = 0
baddest_elf = 0
biggest_baddest_elf = 0

with open('./input.txt', 'r') as f:
	for line in f.readlines():
		line = line.strip()

		# new elf, evaluate and restart
		if line == "":
			if biggest_baddest_elf < elf:
				biggest_elf = baddest_elf
				baddest_elf = biggest_baddest_elf
				biggest_baddest_elf = elf
			elif baddest_elf < elf:
				biggest_elf = baddest_elf
				baddest_elf = elf
			elif biggest_elf < elf:
				biggest_elf = elf

			elf = 0
		else:
			elf += int(line)

print(biggest_baddest_elf)
print(biggest_elf + baddest_elf + biggest_baddest_elf)
