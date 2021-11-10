import math

pen_length = float(input("Length of pendulum (meters): "))

time = (2 * math.pi) * (math.sqrt(pen_length / 9.81))

print(f"Time (seconds): {round(time, 2)}")