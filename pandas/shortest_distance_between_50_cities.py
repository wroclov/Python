from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import geopy.distance
import folium

# List of the 50 largest cities in the world and their coordinates (latitude and longitude)
cities = [
    ("London", 51.5074, -0.1278),
    ("Paris", 48.8566, 2.3522),
    ("Madrid", 40.4168, -3.7038),
    ("Tokyo", 35.6895, 139.6917),
    ("Delhi", 28.7041, 77.1025),
    ("Shanghai", 31.2304, 121.4737),
    ("São Paulo", -23.5505, -46.6333),
    ("Mumbai", 19.0760, 72.8777),
    ("Cairo", 30.0444, 31.2357),
    ("Beijing", 39.9042, 116.4074),
    ("Dhaka", 23.8103, 90.4125),
    ("Mexico City", 19.4326, -99.1332),
    ("Osaka", 34.6937, 135.5023),
    ("Karachi", 24.8607, 67.0011),
    ("Chongqing", 29.5630, 106.5516),
    ("Istanbul", 41.0082, 28.9784),
    ("Buenos Aires", -34.6037, -58.3816),
    ("Kolkata", 22.5726, 88.3639),
    ("Kinshasa", -4.4419, 15.2663),
    ("Lagos", 6.5244, 3.3792),
    ("Manila", 14.5995, 120.9842),
    ("Rio de Janeiro", -22.9068, -43.1729),
    ("Guangzhou", 23.1291, 113.2644),
    ("Lahore", 31.5497, 74.3436),
    ("Shenzhen", 22.5431, 114.0579),
    ("Bangalore", 12.9716, 77.5946),
    ("Moscow", 55.7558, 37.6173),
    ("Tianjin", 39.3434, 117.3616),
    ("Jakarta", -6.2088, 106.8456),
    ("Lima", -12.0464, -77.0428),
    ("Bangkok", 13.7563, 100.5018),
    ("Seoul", 37.5665, 126.9780),
    ("Nagoya", 35.1815, 136.9066),
    ("Hyderabad", 17.3850, 78.4867),
    ("Tehran", 35.6892, 51.3890),
    ("Chicago", 41.8781, -87.6298),
    ("Chengdu", 30.5728, 104.0668),
    ("Nanjing", 32.0603, 118.7969),
    ("Wuhan", 30.5928, 114.3055),
    ("Ho Chi Minh City", 10.8231, 106.6297),
    ("Luanda", -8.8390, 13.2894),
    ("Ahmedabad", 23.0225, 72.5714),
    ("Kuala Lumpur", 3.1390, 101.6869),
    ("Hong Kong", 22.3193, 114.1694),
    ("Dongguan", 23.0207, 113.7518),
    ("Hangzhou", 30.2741, 120.1551),
    ("Foshan", 23.0215, 113.1214),
    ("Shenyang", 41.8057, 123.4315),
    ("Riyadh", 24.7136, 46.6753),
    ("Baghdad", 33.3152, 44.3661)
]


# Calculate the distance matrix between each pair of cities
def compute_distance_matrix(cities):
    distances = []
    for i, (name1, lat1, lon1) in enumerate(cities):
        row = []
        for j, (name2, lat2, lon2) in enumerate(cities):
            if i == j:
                row.append(0)
            else:
                coord1 = (lat1, lon1)
                coord2 = (lat2, lon2)
                distance = geopy.distance.geodesic(coord1, coord2).km
                row.append(distance)
        distances.append(row)
    return distances


distance_matrix = compute_distance_matrix(cities)

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(cities), 1, 0)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)


def distance_callback(from_index, to_index):
    # Convert from routing variable Index to distance matrix NodeIndex
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]


transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Set the parameters for the search
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print the solution and plot the route on a map
if solution:
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    route = []
    leg = 1
    leg_info = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        dist = distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        route_distance += dist
        leg_info.append(
            f'{leg}: {cities[manager.IndexToNode(previous_index)][0]} -> {cities[manager.IndexToNode(index)][0]} ({dist:.2f} km)')
        plan_output += f'{leg}: {cities[manager.IndexToNode(previous_index)][0]} -> {cities[manager.IndexToNode(index)][0]} ({dist:.2f} km)\n'
        leg += 1
    route.append(manager.IndexToNode(index))  # Add the start point to complete the loop

    print(plan_output)
    print('Route distance: {} km'.format(route_distance))

    # Create a map
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add route to the map
    for i in range(len(route) - 1):
        start_city = cities[route[i]]
        end_city = cities[route[i + 1]]
        folium.Marker(location=[start_city[1], start_city[2]], popup=start_city[0]).add_to(m)
        folium.PolyLine(
            locations=[[start_city[1], start_city[2]], [end_city[1], end_city[2]]],
            color='blue',
            tooltip=f'{i + 1}: {start_city[0]} -> {end_city[0]} ({distance_matrix[route[i]][route[i + 1]]:.2f} km)'
        ).add_to(m)

    # Add the start city marker
    start_city = cities[route[0]]
    folium.Marker(location=[start_city[1], start_city[2]], popup=start_city[0], icon=folium.Icon(color='green')).add_to(
        m)

    # Save the map to an HTML file
    m.save("tsp_route.html")

    print("Map saved as tsp_route.html")
else:
    print('No solution found!')
