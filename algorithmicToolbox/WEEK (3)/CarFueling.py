def compute_min_refills(dist, tank, stops):
    if dist <= tank:
        return 0
    
    stops.append(dist)  
    current_stop = 0
    num_stops = 0
    dist_covered = 0
    i = 0
    
    while dist_covered < dist:
        while i < len(stops) and stops[i] - current_stop <= tank:
            i += 1
        if current_stop == stops[i - 1]:  
            return -1
        
        if i == len(stops):  
            break
        
        current_stop = stops[i - 1]
        dist_covered = current_stop
        num_stops += 1

    return num_stops

def main():
    d = int(input("Enter the total distance: "))
    m = int(input("Enter the tank capacity: "))
    n = int(input("Enter the number of stops: "))

    stops = []
    for _ in range(n):
        stops.append(int(input(f"Enter the position of stop {_ + 1}: ")))

    print(compute_min_refills(d, m, stops))

if __name__ == "__main__":
    main()
