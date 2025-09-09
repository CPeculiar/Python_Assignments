# Assignment 1: Design Your Own Class - Superhero Theme! 
# ==========================================================

print("=" * 60)
print("ASSIGNMENT 1: DESIGN YOUR OWN CLASS - SUPERHERO THEME! 🦸‍♂️")
print("=" * 60)

class Superhero:
    """Base Superhero class with common attributes and methods"""
    
    # Class variable (shared by all superheroes)
    hero_count = 0
    
    def __init__(self, name, real_name, power_level=50):
        """Constructor to initialize superhero attributes"""
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.energy = 100
        self.is_active = True
        
        # Increment hero count when new hero is created
        Superhero.hero_count += 1
        print(f"🦸‍♂️ New superhero created: {self.name}!")
    
    def introduce(self):
        """Method to introduce the superhero"""
        print(f"I am {self.name}, also known as {self.real_name}!")
        print(f"Power Level: {self.power_level} | Energy: {self.energy}%")
    
    def use_power(self, power_cost=20):
        """Method to use superhero powers"""
        if self.energy >= power_cost:
            self.energy -= power_cost
            print(f"💥 {self.name} uses their power! Energy remaining: {self.energy}%")
            return True
        else:
            print(f"😴 {self.name} is too tired to use powers!")
            return False
    
    def rest(self):
        """Method to restore energy"""
        self.energy = min(100, self.energy + 30)
        print(f"😌 {self.name} rests and recovers. Energy: {self.energy}%")
    
    @classmethod
    def get_hero_count(cls):
        """Class method to get total number of heroes"""
        return cls.hero_count


# Inheritance Layer 1: Flying Heroes
class FlyingHero(Superhero):
    """Superhero that can fly - demonstrates inheritance"""
    
    def __init__(self, name, real_name, power_level=50, max_altitude=1000):
        super().__init__(name, real_name, power_level)
        self.max_altitude = max_altitude
        self.current_altitude = 0
        self.can_fly = True
    
    def fly(self, altitude=500):
        """Method specific to flying heroes"""
        if altitude > self.max_altitude:
            altitude = self.max_altitude
        
        if self.use_power(15):  # Flying costs energy
            self.current_altitude = altitude
            print(f"🚀 {self.name} soars to {altitude} feet!")
        
    def land(self):
        """Method to land"""
        self.current_altitude = 0
        print(f"🛬 {self.name} lands safely on the ground!")


# Inheritance Layer 2: Speedster Heroes
class SpeedsterHero(Superhero):
    """Superhero with super speed - demonstrates inheritance and encapsulation"""
    
    def __init__(self, name, real_name, power_level=50, max_speed=500):
        super().__init__(name, real_name, power_level)
        self.__max_speed = max_speed  # Private attribute (encapsulation)
        self.current_speed = 0
    
    def run(self, speed=300):
        """Method specific to speedster heroes"""
        if speed > self.__max_speed:
            speed = self.__max_speed
            
        if self.use_power(10):  # Running costs less energy than flying
            self.current_speed = speed
            print(f"💨 {self.name} runs at {speed} mph! Whoosh!")
    
    def get_max_speed(self):
        """Getter method for private max_speed (encapsulation)"""
        return self.__max_speed
    
    def set_max_speed(self, new_speed):
        """Setter method for private max_speed (encapsulation)"""
        if new_speed > 0:
            self.__max_speed = new_speed
            print(f"⚡ {self.name}'s max speed updated to {new_speed} mph!")


# Inheritance Layer 3: Tech Heroes
class TechHero(Superhero):
    """Superhero with technological gadgets"""
    
    def __init__(self, name, real_name, power_level=50, gadgets=None):
        super().__init__(name, real_name, power_level)
        self.gadgets = gadgets if gadgets else ["Basic Scanner", "Communicator"]
        self.suit_power = 100
    
    def use_gadget(self, gadget_name):
        """Method to use technological gadgets"""
        if gadget_name in self.gadgets and self.suit_power >= 20:
            self.suit_power -= 20
            print(f"🔧 {self.name} uses {gadget_name}! Suit power: {self.suit_power}%")
        else:
            print(f"❌ {self.name} can't use {gadget_name} right now!")
    
    def add_gadget(self, gadget_name):
        """Method to add new gadgets"""
        self.gadgets.append(gadget_name)
        print(f"🆕 {self.name} acquired new gadget: {gadget_name}")


# Main execution (only runs when this file is run directly)
if __name__ == "__main__":
    print("\n🌟 Creating our superhero team!")
    print("-" * 40)

    # Create different types of heroes
    superman = FlyingHero("Superman", "Clark Kent", 95, 10000)
    flash = SpeedsterHero("The Flash", "Barry Allen", 85, 1000)
    batman = TechHero("Batman", "Bruce Wayne", 75, ["Batarang", "Grappling Hook", "Batcomputer"])

    print(f"\n📊 Total heroes created: {Superhero.get_hero_count()}")

    print("\n🎬 Hero Introductions:")
    print("-" * 30)
    superman.introduce()
    print()
    flash.introduce()
    print()
    batman.introduce()

    print("\n⚡ Heroes in Action!")
    print("-" * 25)
    superman.fly(5000)
    superman.use_power()
    superman.rest()

    flash.run(800)
    flash.set_max_speed(1200)
    print(f"Flash's max speed: {flash.get_max_speed()} mph")

    batman.use_gadget("Batarang")
    batman.add_gadget("Smoke Bomb")
    batman.use_gadget("Smoke Bomb")

    print("\n✅ Assignment 1 Complete!")
    print("Concepts Demonstrated:")
    print("• Class creation with attributes and methods")
    print("• Constructors (__init__)")
    print("• Inheritance (3 levels)")
    print("• Encapsulation (private attributes)")
    print("• Class and instance variables")
    print("=" * 50)