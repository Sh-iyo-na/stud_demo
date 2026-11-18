# Routing Agent
def decorator(func):
    def wrapper(*args):
        print("\nMonitoring Starting", func.__name__)
        result = func(*args)
        print("Monitoring Completed", func.__name__)
        return result
    return wrapper

def read_route(route_number):
    print("\nEnter Route", route_number, "Details")
    name = input("Route Name: ").strip().title()
    distance = float(input("Distance (km): "))
    traffic = input("Traffic (Low/Medium/Heavy): ").strip().lower()
    time = int(input("Travel Time (minutes): "))
    route = {
        "name": name,
        "distance": distance,
        "traffic": traffic,
        "time": time
    }
    return route

@decorator
def perception():
    n = int(input("Number of routes: "))
    routes = []
    for i in range(1, n + 1):
        route = read_route(i)
        routes.append(route)
    print("\nRoute information received successfully.")
    return routes

@decorator
def processing(routes):
    for route in routes:
        route["name"] = route["name"].strip().title()
        route["traffic"] = route["traffic"].strip().lower()
    print("Route names and traffic information processed.")
    return routes

def reasoning(routes, index=0, suitable=None):
    if suitable is None:
        suitable = []
    if index == len(routes):
        return suitable
    route = routes[index]
    if route["traffic"] == "heavy":
        print(route["name"], "-> Heavy Traffic -> Rejected")
    elif route["traffic"] in ["low", "medium"]:
        print(route["name"], "->", route["traffic"].title(),
              "Traffic -> Suitable")
        suitable.append(route)
    else:
        print(route["name"], "-> Invalid Traffic Information -> Rejected")
    return reasoning(routes, index + 1, suitable)

def decision(suitable_routes):
    if len(suitable_routes) == 0:
        print("No suitable routes available.")
        return None
    best_route = min(
        suitable_routes,
        key=lambda route: route["time"]
    )
    print("Best Route:", best_route["name"])
    return best_route

@decorator
def action(best_route):
    if best_route is None:
        print("No suitable route can be recommended.")
        return

    print("\n ROUTE RECOMMENDATION ")
    print("Recommended Route:", best_route["name"])
    print("Distance:", best_route["distance"], "km")
    print("Travel Time:", best_route["time"], "minutes")
    print("Traffic:", best_route["traffic"].title())
    print("Reason: Lowest travel time with acceptable traffic condition.")
    print("\nAgent Status: DECISION COMPLETED")

def route_agent():
    routes = perception()
    routes = processing(routes)
    print("\n[Reasoning Function]")
    suitable_routes = reasoning(routes)
    best_route = decision(suitable_routes)
    action(best_route)

route_agent()