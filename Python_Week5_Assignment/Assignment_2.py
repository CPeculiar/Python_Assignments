# Assignment 2: Polymorphism Challenge - Transportation! 🚗✈️
# ===========================================================

print("=" * 60)
print("ASSIGNMENT 2: POLYMORPHISM CHALLENGE - TRANSPORTATION! 🚗✈️")
print("=" * 60)

class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, name, fuel=100):
        self.name = name
        self.fuel = fuel
        self.position = "Starting Point"
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        print(f"🚀 {self.name} is moving somehow...")
    
    def refuel(self):
        """Method to refuel the vehicle"""
        self.fuel = 100
        print(f"⛽ {self.name} has been refueled!")
    
    def status(self):
        """Show vehicle status"""
        print(f"📍 {self.name} | Fuel: {self.fuel}% | Location: {self.position}")


class Car(Vehicle):
    """Car class - demonstrates polymorphism with move()"""
    
    def __init__(self, name, brand="Generic", fuel=100):
        super().__init__(name, fuel)
        self.brand = brand
        self.wheels = 4
    
    def move(self):
        """Car-specific move method"""
        if self.fuel >= 10:
            self.fuel -= 10
            self.position = "Highway"
            print(f"🚗 {self.name} ({self.brand}) is driving on the road! Vroom vroom!")
        else:
            print(f"⛽ {self.name} needs fuel to drive!")
    
    def honk(self):
        """Car-specific method"""
        print(f"📯 {self.name} goes BEEP BEEP!")


class Plane(Vehicle):
    """Plane class - demonstrates polymorphism with move()"""
    
    def __init__(self, name, airline="Generic Air", fuel=100):
        super().__init__(name, fuel)
        self.airline = airline
        self.altitude = 0
    
    def move(self):
        """Plane-specific move method"""
        if self.fuel >= 20:
            self.fuel -= 20
            self.altitude = 35000
            self.position = "In the Sky"
            print(f"✈️ {self.name} ({self.airline}) is flying through the clouds at {self.altitude} feet!")
        else:
            print(f"⛽ {self.name} needs fuel to fly!")
    
    def land(self):
        """Plane-specific method"""
        self.altitude = 0
        self.position = "Airport"
        print(f"🛬 {self.name} has landed safely at the airport!")


class Boat(Vehicle):
    """Boat class - demonstrates polymorphism with move()"""
    
    def __init__(self, name, boat_type="Speedboat", fuel=100):
        super().__init__(name, fuel)
        self.boat_type = boat_type
    
    def move(self):
        """Boat-specific move method"""
        if self.fuel >= 15:
            self.fuel -= 15
            self.position = "Open Waters"
            print(f"🚤 {self.name} ({self.boat_type}) is sailing across the water! Splash splash!")
        else:
            print(f"⛽ {self.name} needs fuel to sail!")
    
    def anchor(self):
        """Boat-specific method"""
        self.position = "Anchored"
        print(f"⚓ {self.name} has dropped anchor and is staying put!")


class Bicycle(Vehicle):
    """Bicycle class - demonstrates polymorphism (no fuel needed!)"""
    
    def __init__(self, name, bike_type="Mountain Bike"):
        super().__init__(name, fuel=0)  # Bicycles don't need fuel!
        self.bike_type = bike_type
    
    def move(self):
        """Bicycle-specific move method"""
        self.position = "Bike Path"
        print(f"🚴‍♂️ {self.name} ({self.bike_type}) is pedaling along the bike path! Eco-friendly!")
    
    def refuel(self):
        """Override refuel for bicycles"""
        print(f"🥤 {self.name} doesn't need fuel, but the rider could use some water!")
    
    def ring_bell(self):
        """Bicycle-specific method"""
        print(f"🔔 {self.name} goes RING RING!")


# Main execution (only runs when this file is run directly)
if __name__ == "__main__":
    print("\n🚀 Creating our transportation fleet!")
    print("-" * 45)

    # Create different vehicles
    vehicles = [
        Car("Lightning McQueen", "Racing Car"),
        Plane("Sky Dancer", "CloudNine Airlines"),
        Boat("Ocean Explorer", "Yacht"),
        Bicycle("Green Machine", "Electric Bike")
    ]

    print("📋 Vehicle Status Check:")
    print("-" * 30)
    for vehicle in vehicles:
        vehicle.status()

    print("\n🎬 Polymorphism in Action - All vehicles move differently!")
    print("-" * 65)

    # This demonstrates POLYMORPHISM - same method name, different behaviors
    for vehicle in vehicles:
        print(f"\n🎯 {vehicle.name}'s turn:")
        vehicle.move()  # Each vehicle moves differently!
        vehicle.status()

    print("\n🔧 Specific Vehicle Actions:")
    print("-" * 35)

    # Demonstrate unique methods for each vehicle type
    vehicles[0].honk()  # Car method
    vehicles[1].land()  # Plane method
    vehicles[2].anchor()  # Boat method
    vehicles[3].ring_bell()  # Bicycle method

    # Refuel all vehicles (another example of polymorphism)
    print("\n⛽ Refueling Time!")
    print("-" * 20)
    for vehicle in vehicles:
        vehicle.refuel()  # Each vehicle handles refueling differently

    print("\n✅ Assignment 2 Complete!")
    print("Polymorphism Concepts Demonstrated:")
    print("• Same method name (move()) with different implementations")
    print("• Method overriding (refuel() for bicycles)")
    print("• Base class provides structure")
    print("• Subclasses provide specific behavior")
    print("=" * 50)