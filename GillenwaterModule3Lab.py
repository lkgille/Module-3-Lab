"""
Module 3 Lab - Case Study: Lists, Functions, and Classes
Lillian Gillenwater
File Name: GillenwaterModule3Lab

"""

class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def display_info(self):
        # Function can be called to display the data that will be input
        print("Vehicle type: " + self.vehicle_type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Doors: " + self.doors)
        print("Roof: " + self.roof)

# Allow the user to input the information
print("Input the car's details:")
vehicle_type = "car"
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Number of doors (2 or 4): ")
roof = input("Type of roof (solid or sunroof): ")

car = Automobile(vehicle_type, year, make, model, doors, roof)

print("\nData input: ")
car.display_info() # Displays the info that was input