import time

print("=== COUNTDOWN TIMER ===")

# Get input from user
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# Convert everything to total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

print(f"\n⏰ Timer set for: {hours:02d}:{minutes:02d}:{seconds:02d}")
input("Press Enter to start...")

# Countdown loop
for remaining in range(total_seconds, -1, -1):
    # Calculate current hours, minutes, seconds
    h = remaining // 3600
    m = (remaining % 3600) // 60
    s = remaining % 60
    
    # Display in HH:MM:SS format
    print(f"⏳ {h:02d}:{m:02d}:{s:02d} remaining", end='\r')
    time.sleep(1)

print("\n🎉 TIME'S UP! 🎉")
print("🔔 Ding ding ding!")