import math

width = float(input("Enter the width of the tire in mm: "))
aspect = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

volume = float(((math.pi * width * width * aspect) * ((width * aspect) + (2540 * diameter)))/10000000000)

volume_round = "{:.2f}".format(volume)

print(f"The volume of the tire is {volume_round}")

from datetime import datetime
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")

model = "GMC Acadia"
length = 193
width = 75
height = 67

with open("dimensions.txt", "at") as dimens_file:
    print(model, file=dimens_file)
    print(f"{length}, {width}, {height}", file=dimens_file)
    