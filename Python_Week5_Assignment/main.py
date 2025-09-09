# Main runner to execute both assignments
# =====================================

print("🎓 WEEK 5 PYTHON ASSIGNMENTS")
print("=" * 40)
print("Running both assignments...")
print()

# Option 1: Import and run both assignments
try:
    print("🏃‍♂️ Running Assignment 1...")
    import assignment1_superheroes
    
    print("\n" + "=" * 60)
    print()
    
    print("🏃‍♂️ Running Assignment 2...")
    import assignment2_polymorphism
    
except ImportError as e:
    print(f"❌ Error importing files: {e}")
    print("Make sure all files are in the same directory!")

print("\n🎉 Both assignments completed!")
print("=" * 40)

# Optional: You can also run them individually
print("\n💡 USAGE OPTIONS:")
print("1. Run this file (main.py) to execute both assignments")
print("2. Run 'python assignment1_superheroes.py' for just Assignment 1")
print("3. Run 'python assignment2_polymorphism.py' for just Assignment 2")
print("4. Keep everything in one file (week5_assignment.py) if preferred")