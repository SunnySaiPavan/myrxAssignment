arrival = ["8:00", "8:05","8:10", "8:15", "8:20"]
depature = ["8:30", "8:25", "8:35", "8:40", "8:50"]

def convert_hours_into_mins(arrival, departure):
    arr_in_mins = []
    dep_in_mins = []
    for i in range(len(arrival)):
        arrival_split = arrival[i].split(":")
        departure_split = departure[i].split(":")
        arrival_hours = int(arrival_split[0])
        departure_hours = int(departure_split[0])
        arrival_mins = int(arrival_split[1])
        departure_mins = int(departure_split[1])
        arr_in_mins.append(arrival_hours*60+arrival_mins)
        dep_in_mins.append(departure_hours*60+departure_mins)
    return arr_in_mins,dep_in_mins

def max_platforms_needed(arrival, departure):
    if len(arrival) == 0 or len(departure) == 0:
        return 0
    elif len(arrival) != len(departure):
        return 0
    else:
        a_in_minutes, d_in_minutes = convert_hours_into_mins(arrival, departure)
        max_platforms = 1
        for i in range(len(arrival)):
            platforms_needed = 1
            for j in range(i):
                if a_in_minutes[i] < d_in_minutes[j]:
                    platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
        return max_platforms
result = max_platforms_needed(arrival, depature)
print("platforms needed are:", result)                
    
