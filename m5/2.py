# SMARTROUTE AGENT OBJECT INTELLIGENCE FRAMEWORK

def decorator(func):
    def wrapper(*args):
        print("\nMonitoring Starting", func.__name__)
        result = func(*args)
        print("Monitoring Completed", func.__name__)
        return result
    return wrapper

# Traffic class
class Traffic:
    def __init__(self, condition):
        self.condition = condition.strip().lower()
    def get_condition(self):
        return self.condition

# Route class
class Route:
    def __init__(self, name, distance, traffic, time):
        self.name = name.strip().title()
        self.distance = distance
        self.traffic = Traffic(traffic)
        self.time = time
    def display(self):
        print("\nRoute Name:", self.name)
        print("Distance:", self.distance, "km")
        print("Traffic:", self.traffic.get_condition().title())
        print("Travel Time:", self.time, "min")
    def check_suitability(self):
        condition = self.traffic.get_condition()
        if condition == "heavy":
            return False
        elif condition in ["low", "medium"]:
            return True
        else:
            return False

# Highway class
class HighwayRoute(Route):
    def check_suitability(self):
        condition = self.traffic.get_condition()
        if condition == "heavy":
            return False
        elif condition in ["low", "medium"]:
            return True
        else:
            return False

# City class
class CityRoute(Route):
    def check_suitability(self):
        condition = self.traffic.get_condition()
        if condition == "heavy":
            return False
        elif condition in ["low", "medium"]:
            return True
        else:
            return False

# Smart route agent class
class SmartRouteAgent:
    def __init__(self):
        self.routes = []

    @decorator
    def perception(self):
        n = int(input("Number of routes: "))
        for i in range(1, n + 1):
            print("\nEnter Route", i, "Details")
            name = input("Route Name: ")
            distance = float(input("Distance (km): "))
            traffic = input("Traffic (low/medium/heavy): ")
            time = int(input("Travel time (min): "))
            route_type = input("Route Type (highway/city): ").strip().lower()
            if route_type == "highway":
                route = HighwayRoute(name, distance, traffic, time)
            elif route_type == "city":
                route = CityRoute(name, distance, traffic, time)
            else:
                route = Route(name, distance, traffic, time)
            self.routes.append(route)
        print("\nRoute information received.")

    @decorator
    def processing(self):
        for route in self.routes:
            route.name = route.name.strip().title()
        print("Route information processed.")

    def reasoning(self, index=0, suitable=None):
        if suitable is None:
            suitable = []
        if index == len(self.routes):
            return suitable
        route = self.routes[index]
        if route.check_suitability():
            print(route.name, route.traffic.get_condition().title(),
                  "Traffic -> Suitable")
            suitable.append(route)
        else:
            print(route.name, "-> Not Suitable")
        return self.reasoning(index + 1, suitable)

    def decision(self, suitable_routes):
        if len(suitable_routes) == 0:

            print("No suitable routes available.")
            return None
        best_route = min(
            suitable_routes,
            key=lambda route: route.time
        )
        print("\nBest Route:", best_route.name)
        return best_route
    
    @decorator
    def display(self, best_route):
        if best_route is None:
            print("No suitable route.")
            return
        print("\nROUTE RECOMMENDATION")
        print("Recommended Route:", best_route.name)
        print("Distance:", best_route.distance, "km")
        print("Travel Time:", best_route.time, "min")
        print("Traffic:",
              best_route.traffic.get_condition().title())
        print("Reason: Lowest travel time and good traffic condition.")
        print("Agent Status: DECISION COMPLETED")

    def route(self):
        print("\nAgent Created: SmartRouteAgent")
        self.perception()
        self.processing()
        print("\nReasoning Function")
        suitable_routes = self.reasoning()
        print("\nAgent Decision")
        best_route = self.decision(suitable_routes)
        self.display(best_route)

# main program
print("Smart Route Agent")
agent = SmartRouteAgent()
agent.route()