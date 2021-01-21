# Глава 6. Поиск в ширину
import collections

def search(name):
	search_queue = collections.deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(f'{person} is a mango seller!')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	print('Mango seller not found')
	return False

def person_is_seller(name): return name[-1] == 'm'

graph = {}
graph['you'] = ['Alice', 'Bob', 'Claire']
graph['Alice'] = ['Peggy']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Claire'] = ['Thom', 'Jonny']
graph['Peggy'] = []
graph['Anuj'] = []
graph['Thom'] = []
graph['Jonny'] = []

search('you')