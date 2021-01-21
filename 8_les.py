# Глава 8. Жадные алгоритмы

def greed_alg(stations, states):
	final_stations = set()
	while states:
		best_station = None
		states_covered = set()
		for station, states_for_station in stations.items():
			covered = states & states_for_station
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered
		states -= states_covered
		final_stations.add(best_station)
	return final_stations

states = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

print(greed_alg(stations, states))