# Smart Routing Agent
# Traffic class
class Traffic:
    def __init__(self, condition):
        self.condition = condition

    def get_traffic(self):
        return self.condition

# Route class
class Route:
    def __init__(self, name, distance, traffic, travel_time):
        self.name = name
        self.distance = distance
        self.traffic = Traffic(traffic)
        self.travel_time = travel_time

    def display(self):
        print("\n", self.name)
        print("Distance    :", self.distance, "km")
        print("Traffic     :", self.traffic.get_traffic())
        print("Travel Time :", self.travel_time, "min")

    def check_suitability(self):
        condition = self.traffic.get_traffic().strip().lower()
        if condition == "heavy":
            return "Not Suitable"
        elif condition in ["low", "medium"]:
            return "Suitable"
        else:
            return "Not Suitable"

# Highway class
class HighwayRoute(Route):
    def check_suitability(self):
        condition = self.traffic.get_traffic().strip().lower()
        if condition == "heavy":
            return "Not Suitable"
        elif condition in ["low", "medium"]:
            return "Suitable"
        else:
            return "Not Suitable"

# City class
class CityRoute(Route):
    def check_suitability(self):
        condition = self.traffic.get_traffic().strip().lower()
        if condition == "heavy":
            return "Not Suitable"
        elif condition in ["low", "medium"]:
            return "Suitable"
        else:
            return "Not Suitable"

# Agent class
class SmartRouteAgent:
    def __init__(self):
        self.routes = []

    def read_routes(self):
        n = int(input("\nNumber of routes: "))
        for i in range(1, n + 1):
            print("\nEnter Route", i, "Details")
            name = input("Route Name: ")
            distance = float(input("Distance (km): "))
            traffic = input("Traffic (Low/Medium/Heavy): ").strip().title()
            travel_time = int(input("Travel Time (min): "))
            route_type = input("Route Type (Highway/City): ").strip().lower()

            if route_type == "highway":
                route = HighwayRoute(name, distance, traffic, travel_time)
            elif route_type == "city":
                route = CityRoute(name, distance, traffic, travel_time)
            else:
                route = Route(name, distance, traffic, travel_time)
            self.add_route(route)
        print("\nRoute information received.")

    def add_route(self, route):
        self.routes.append(route)

    def analyse_routes(self):
        print("\nAgent Analysis:")
        suitable_routes = []
        for route in self.routes:
            result = route.check_suitability()
            print(route.name, "->", result)
            if result == "Suitable":
                suitable_routes.append(route)
        return suitable_routes

    def make_decision(self):
        suitable_routes = self.analyse_routes()
        if len(suitable_routes) == 0:
            print("\nNo Suitable Route Available")
            return None
        best_route = min(
            suitable_routes,
            key=lambda route: route.travel_time
        )
        return best_route

    def recommend_route(self):
        best_route = self.make_decision()
        print("\nAgent Decision:")
        if best_route:
            print("Recommended Route ->", best_route.name)
            print("\nFinal Action:")
            print(best_route.name, "recommended to the user.")
        else:
            print("No route can be recommended.")

# Main program
print("SMARTROUTE AGENT")
agent = SmartRouteAgent()
agent.read_routes()
print("\nAvailable Route Objects:")
for route in agent.routes:
    route.display()
agent.recommend_route()
