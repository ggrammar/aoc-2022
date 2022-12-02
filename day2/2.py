OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

MY_ROCK = "X"
MY_PAPER = "Y"
MY_SCISSORS = "Z"

WIN = 6
DRAW = 3
LOSS = 0

ROCK_VALUE = 1
PAPER_VALUE = 2
SCISSORS_VALUE = 3

LOSE_RESULT = "X"
DRAW_RESULT = "Y"
WIN_RESULT = "Z"

def value_of(choice):
	if choice == MY_ROCK:
		return ROCK_VALUE
	elif choice == MY_SCISSORS:
		return SCISSORS_VALUE
	else:
		return PAPER_VALUE

def score(opponent, me):

	ret_val = 0

	if opponent == OPPONENT_ROCK:
		if me == MY_ROCK:
			ret_val = DRAW
		elif me == MY_PAPER:
			ret_val = WIN
		elif me == MY_SCISSORS:
			ret_val = LOSS

	elif opponent == OPPONENT_PAPER:
		if me == MY_ROCK:
			ret_val = LOSS
		elif me == MY_PAPER:
			ret_val = DRAW
		elif me == MY_SCISSORS:
			ret_val = WIN

	elif opponent == OPPONENT_SCISSORS:
		if me == MY_ROCK:
			ret_val = WIN
		elif me == MY_PAPER:
			ret_val = LOSS
		elif me == MY_SCISSORS:
			ret_val = DRAW
			
	return ret_val + value_of(me)


def part_2_score(opponent, result):

	if opponent == OPPONENT_ROCK:
		if result == WIN_RESULT:
			ret_val = WIN
			my_choice = PAPER_VALUE
		elif result == DRAW_RESULT:
			ret_val = DRAW
			my_choice = ROCK_VALUE
		elif result == LOSE_RESULT:
			ret_val = LOSS
			my_choice = SCISSORS_VALUE

	elif opponent == OPPONENT_PAPER:
		if result == WIN_RESULT:
			ret_val = WIN
			my_choice = SCISSORS_VALUE
		elif result == DRAW_RESULT:
			ret_val = DRAW
			my_choice = PAPER_VALUE
		elif result == LOSE_RESULT:
			ret_val = LOSS
			my_choice = ROCK_VALUE

	elif opponent == OPPONENT_SCISSORS:
		if result == WIN_RESULT:
			ret_val = WIN
			my_choice = ROCK_VALUE
		elif result == DRAW_RESULT:
			ret_val = DRAW
			my_choice = SCISSORS_VALUE
		elif result == LOSE_RESULT:
			ret_val = LOSS
			my_choice = PAPER_VALUE

	return ret_val + my_choice

with open("input.txt", "r") as f:
	total_score = 0
	part_2_total_score = 0

	for line in f.readlines():
		line = line.strip()
		OPPONENT_CHOICE, MY_CHOICE = line.split(" ")
		total_score += score(OPPONENT_CHOICE, MY_CHOICE)

		OPPONENT_CHOICE, DESIRED_RESULT = line.split(" ")
		part_2_total_score += part_2_score(OPPONENT_CHOICE, DESIRED_RESULT)

print(total_score)
print(part_2_total_score)


		
