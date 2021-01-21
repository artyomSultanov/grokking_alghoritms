# Глава 1. Бинарный поиск
def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = int((low + high) / 2)
		guess = list[mid]

		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


my_list = [i for i in range(100)]

print(binary_search(my_list, 49))
print(binary_search(my_list, 0))