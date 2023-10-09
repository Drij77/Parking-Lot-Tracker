class ParkingLot:
    def __init__(self):
        self.levels = {"A": [False] * 20, "B": [False] * 20}
        self.vehicle_map = {}

    def assign_parking_spot(self, vehicle_number):

        if str(vehicle_number) in self.vehicle_map:
            return f"Vehicle with number {vehicle_number} is already parked at Level {self.vehicle_map[vehicle_number]['level']}, Spot {self.vehicle_map[vehicle_number]['spot']}"

        for level, spots in self.levels.items():
            for spot_number, is_occupied in enumerate(spots):
                if not is_occupied:
                    self.vehicle_map[vehicle_number] = {"level": level, "spot": spot_number + 1}
                    self.levels[level][spot_number] = True
                    return {"level": level, "spot": spot_number + 1}
        return "Parking is full"

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_map:
            return self.vehicle_map[vehicle_number]
        return "Vehicle not found in the parking lot"


def main():
    parking_lot = ParkingLot()

    while True:
        print("\nParking Lot Tracker")
        print("1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(result if isinstance(result, dict) else result)
        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result if isinstance(result, dict) else "Vehicle not found in the parking lot")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
