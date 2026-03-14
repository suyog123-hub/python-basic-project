print("🔄 WORD REVERSER")

while True:
    word = input("\nEnter a word (or 'quit'): ")
    if word.lower() == 'quit':
        break
    print(f"Reversed: {word[::-1]}")
    print(f"Length: {len(word)} letters")
    print(f"Uppercase: {word.upper()}")