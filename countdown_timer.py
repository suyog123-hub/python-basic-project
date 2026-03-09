import time

seconds = int(input("Seconds: "))
for i in range(seconds, 0, -1):
    print(f"⏰ {i} seconds left", end='\r')
    time.sleep(1)
print("🎉 Time's up!   ")