#!/usr/bin/python3

vehicle_type = "Automobile"

class vehicle:
    vehicle_count = 0

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        vehicle.vehicle_count += 1
    def display_info(self):
        return f"{self.brand} {self.year} {vehicle_type} Count Them: {self.vehicle_count}"
vehicle1 = vehicle("Toyota", 2022)
vehicle2 = vehicle("RAVA4", 2020)

print(vehicle1.display_info())
print(vehicle2.display_info())
print(f"total vehicles: {vehicle.vehicle_count}")
