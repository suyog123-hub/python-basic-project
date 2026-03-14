print("🔄 WORD REVERSER")

while True:
    word = input("\nEnter a word (or 'quit'): ")
    if word.lower() == 'quit':
        break
    print(f"Reversed: {word[::-1]}")