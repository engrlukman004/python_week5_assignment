# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is now powered on!"

    def power_off(self):
        return f"{self.brand} {self.model} is now powered off!"

# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Initialize attributes from the base class
        self.os = os
        self.storage = storage

    # Method to display smartphone info
    def display_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Storage: {self.storage}GB"

    # Method to simulate taking a photo
    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo!"

# Another derived class to explore polymorphism
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    # Overriding power_on method
    def power_on(self):
        return f"The {self.brand} {self.model} tablet with a {self.screen_size}-inch screen is now on!"

# Testing the classes
# Create instances of Smartphone and Tablet
smartphone = Smartphone(brand="Apple", model="iPhone 14", os="iOS", storage=128)
tablet = Tablet(brand="Samsung", model="Galaxy Tab S8", screen_size=12.4)

# Using methods
print(smartphone.display_specs())
print(smartphone.take_photo())
print(smartphone.power_on())

print(tablet.power_on())
print(tablet.power_off())
