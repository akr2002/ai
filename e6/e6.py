class Frame:
    def __init__(self, name, attributes=None, parent=None):
        self.name = name  # Name of the frame (e.g., "Car")
        self.attributes = attributes if attributes is not None else {}
        self.parent = parent  # Parent frame for inheritance

    def set_attribute(self, key, value):
        """Set or update an attribute in the frame."""
        self.attributes[key] = value

    def get_attribute(self, key):
        """Retrieve an attribute's value. If not found, check the parent frame."""
        if key in self.attributes:
            return self.attributes[key]
        elif self.parent is not None:
            return self.parent.get_attribute(key)
        else:
            return None

    def __repr__(self):
        return f"Frame(name={self.name}, attributes={self.attributes})"


# Base Frame for all vehicles
vehicle_frame = Frame("Vehicle")
vehicle_frame.set_attribute("type", "Transportation")
vehicle_frame.set_attribute("wheels", 4)

# Specific Frame for a car, inheriting from vehicle
car_frame = Frame("Car", parent=vehicle_frame)
car_frame.set_attribute("fuel", "Gasoline")

# Specific Frame for a bicycle, inheriting from vehicle
bicycle_frame = Frame("Bicycle", parent=vehicle_frame)
bicycle_frame.set_attribute("wheels", 2)  # Override the wheels attribute
bicycle_frame.set_attribute("fuel", "None")

# Specific Frame for an electric car, inheriting from car
electric_car_frame = Frame("ElectricCar", parent=car_frame)
electric_car_frame.set_attribute("fuel", "Electricity")

attributes = ["type", "fuel", "wheels"]
# Access attributes from the car frame
print("Car frame attributes")
print("====================")
for attribute in attributes:
    print(attribute, "\t: ", car_frame.get_attribute(attribute))

print("\nBicycle frame attributes")
print("========================")
for attribute in attributes:
    print(attribute, "\t: ", bicycle_frame.get_attribute(attribute))

print("\nElectric car frame attributes")
print("=============================")
for attribute in attributes:
    print(attribute, "\t: ", electric_car_frame.get_attribute(attribute))
