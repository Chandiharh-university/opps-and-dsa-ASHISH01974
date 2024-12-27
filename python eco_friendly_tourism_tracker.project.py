class EcoFriendlyTourismTracker:
    def __init__(self):
        self.trips = []
        self.eco_friendly_destinations = [
            "Costa Rica",
            "Norway",
            "New Zealand",
            "Bhutan",
            "Iceland"
        ]

    def add_trip(self, destination, distance_km, transport_mode):
        carbon_factor = self.get_carbon_factor(transport_mode)
        carbon_footprint = distance_km * carbon_factor
        self.trips.append({
            'destination': destination,
            'distance_km': distance_km,
            'transport_mode': transport_mode,
            'carbon_footprint': carbon_footprint
        })

    def get_carbon_factor(self, transport_mode):
        # Carbon factors in kg CO2 per km
        transport_modes = {
            'plane': 0.15,
            'car': 0.12,
            'train': 0.03,
            'bus': 0.05,
            'bike': 0.00,
            'walk': 0.00
        }
        return transport_modes.get(transport_mode, 0.00)

    def calculate_total_carbon_footprint(self):
        total_carbon = sum(trip['carbon_footprint'] for trip in self.trips)
        return total_carbon

    def list_eco_friendly_destinations(self):
        return self.eco_friendly_destinations

def main():
    tracker = EcoFriendlyTourismTracker()
    
    while True:
        print("\nEco-Friendly Tourism Tracker")
        print("1. Add a trip")
        print("2. Calculate total carbon footprint")
        print("3. List eco-friendly destinations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            destination = input("Enter destination: ")
            distance_km = input("Enter distance (in km): ")
            try:
                distance_km = float(distance_km)
            except ValueError:
                print("Please enter a valid number for distance.")
                continue
            transport_mode = input("Enter transport mode (plane, car, train, bus, bike, walk): ").lower()
            if transport_mode not in ['plane', 'car', 'train', 'bus', 'bike', 'walk']:
                print("Please enter a valid transport mode.")
                continue
            tracker.add_trip(destination, distance_km, transport_mode)
            print("Trip added successfully!")
        elif choice == '2':
            total_carbon_footprint = tracker.calculate_total_carbon_footprint()
            print(f"Total Carbon Footprint: {total_carbon_footprint:.2f} kg CO2")
        elif choice == '3':
            eco_destinations = tracker.list_eco_friendly_destinations()
            print("Eco-friendly Destinations:")
            for destination in eco_destinations:
                print(f"- {destination}")
        elif choice == '4':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()