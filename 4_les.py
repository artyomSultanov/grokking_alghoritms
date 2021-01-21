# Глава 4. Быстрая сортировка
def my_sum(x):
	if x == []:
		return 0
	else:
		return x.pop() + my_sum(x)
		
print(my_sum([1, 2, 3]))

def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]

		greater = [i for i in arr[1:] if i > pivot]

		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))