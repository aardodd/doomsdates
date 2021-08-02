sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

doomsdates = {
	(False,  1): [3, 10, 17, 24, 31],
	(True,   1): [4, 11, 18, 25],
	(False,  2): [7, 14, 21, 28],
	(True,   2): [1, 8, 15, 22, 29],
	(False,  3): [7, 14, 21, 28],
	(False,  4): [4, 11, 18, 25],
	(False,  5): [2, 9, 16, 23, 30],
	(False,  6): [6, 13, 20, 27],
	(False,  7): [4, 11, 18, 25],
	(False,  8): [1, 8, 15, 22, 29],
	(False,  9): [5, 12, 19, 26],
	(False, 10): [3, 10, 17, 24, 31],
	(False, 11): [7, 14, 21, 28],
	(False, 12): [5, 12, 19, 26],
}

def friendly_doomsday(weekday):
	if weekday == sunday:
		return "sunday"
	elif weekday == monday:
		return "monday"
	elif weekday == tuesday:
		return "tuesday"
	elif weekday == wednesday:
		return "wednesday"
	elif weekday == thursday:
		return "thursday"
	elif weekday == friday:
		return "friday"
	elif weekday == saturday:
		return "saturday"

def absolute(x):
	if x < 0:
		return -x
	return x

def difference(x, y):
	if x < y:
		return y - x
	return x - y

def anchor_day(year):
	interval = absolute(year) % 400
	if interval <= 99:
		return tuesday
	elif interval <= 199:
		return sunday
	elif interval <= 299:
		return friday
	elif interval <= 399:
		return wednesday

def calculate_doomsday(year):
	interval = year % 100

	step_one = interval // 12
	step_two = difference(interval, step_one * 12)
	step_three = step_two // 4
	step_four = anchor_day(year)
	step_five = step_one + step_two + step_three + step_four

	return step_five - ((step_five // 7) * 7)

def closest_doomsdate(year, month, day):
	is_leapyear = year % 4 == 0
	shortest = 1000

	for d in doomsdates[(is_leapyear and month <= 2, month)]:
		if difference(day, d) <= shortest:
			shortest = d

	return shortest


year = int(input("Enter year (1-9999): "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))

dday = calculate_doomsday(year)
closest = closest_doomsdate(year, month, day)
diff = difference(day, closest)

# count backwards from the closest day if its further ahead than the provided day
if closest > day:
	diff = -diff

print(str(year) + "-" + str(month) + "-" + str(day) + " is a " + friendly_doomsday((dday + diff) % 7))
