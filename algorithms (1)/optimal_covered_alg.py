
def optimal_covered(states_needed, stations):
    states_needed = set(states_needed)
    used_stations = []
    used_states = []

    while states_needed:
        non_used_stations = set(stations) - set(used_stations)
        best_station = None
        for station in non_used_stations:
            new_states = set(stations[station]) - set(used_states)
            
            if not new_states & states_needed:
                continue
            
            if len(new_states) > len( stations.get(best_station, []) ):
                best_station = station
        
        used_stations.append(best_station)
        used_states += stations[best_station]
        states_needed -= set(used_states)
        
    return used_stations
        


states_needed = ["wa", "mt", "id", "or", "nv", "ut", "ca", "az"]
stations = {"one": ["id", "nv", "ut"],
            "two": ["wa", "mt", "id"],
            "three": ["or", "ca", "nv"],
            "four": ["nv", "ut"],
            "five": ["ca", "az"]}


if __name__ == "__main__":
    print("need:", states_needed)
    print("\nstations:", stations)
    print( "\nyou should to used", optimal_covered(states_needed[:], stations.copy()) )

    print()
    print("Это всего лишь алгоритм!")
    print("Вся его суть в коде")
    input("Press enter to continue...")
