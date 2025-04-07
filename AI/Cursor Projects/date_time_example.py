from datetime import datetime

# Get current date and time
now = datetime.now()
print("Current date and time:", now)

# Format as string in different formats
print("Formatted date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Date only:", now.strftime("%Y-%m-%d"))
print("Time only:", now.strftime("%H:%M:%S"))
print("Custom format:", now.strftime("%d %B, %Y %I:%M %p"))

# Access individual components
print("\nDate components:")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("\nTime components:")
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second) 