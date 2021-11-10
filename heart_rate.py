age = int(input("Please enter your age: "))

rate_max = 220 - age

rate_lower = ((rate_max) * 0.65)

rate_upper = ((rate_max) * 0.85)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {round(rate_lower)} and {round(rate_upper)} beats per minute.")