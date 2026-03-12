import random

print("🎲 DICE ROLLER 🎲")
while True:
    input("Press Enter to roll (q to quit)")
    dice = random.randint(1, 6)
    print(f"┌─────┐")
    print(f"│  {dice}  │")
    print(f"└─────┘")
    
    if input("Roll again? (y/n): ").lower() == 'n':
        break