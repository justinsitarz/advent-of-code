import itertools
from password_list import passwords

start = 128392
end = 643281

def advanced_password_checker(password_list):
	count = 0
	advanced_consecutive = False
	for num in password_list:
		digits_list = [int(x) for x in str(num)]
		advanced_consecutive = advanced_consecutive_checker(digits_list)
		if advanced_consecutive:
			print(num)
			count += 1
	print(count)
		

def password_checker(start, end):
	increasing = False
	consecutive = False
	count = 0
	for num in range(start, end+1):
		digits_list = [int(x) for x in str(num)]
		increasing = increasing_checker(digits_list)
		consecutive = consecutive_checker(digits_list)
		if increasing and consecutive:
			print(num)
			count += 1
	print(count)

def increasing_checker(digits_list):
	max_so_far = digits_list[0]
	for d in digits_list:
		if d >= max_so_far:
			max_so_far = d
		else: 
			return False
	return True

def consecutive_checker(digits_list):
	for x, y in itertools.groupby(digits_list):
		if len(list(y)) >= 2:
			return True
	return False

def advanced_consecutive_checker(digits_list):
	for x, y in itertools.groupby(digits_list):
		if len(list(y)) == 2:
			return True
	return False

# password_checker(start, end)
advanced_password_checker(passwords)