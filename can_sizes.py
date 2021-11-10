import math 

radius_list= [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
height_list = [10.16, 11.91, 11.59, 11.91, 10.79, 14.29, 8.89, 6.83, 17.78, 12.38, 11.27, 11.11]
can_names_list= ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6oz', '#8oz short', '#10', '#211', '#300', '#303']
cost_per_can = [.28, .43, .45, .61, .86, .83, .22, .26, 1.53, .34, .38, .42]

def main():
    for i in range(11):
        radius = radius_list[i]
        height = height_list[i]
        cost = cost_per_can[i]
        can_name = can_names_list[i]
        #can_name = input("Please enter the name of the can: ")
        #radius = float(input("Please enter can radius in centimeters: "))
        #height = float(input("Please enter the height of the can in centimeters: "))
        #cost = float(input("Please put in the cost of the can: "))
        volume = cylinder_volume(radius, height)
        surface_area = cylinder_surface_area(radius, height)
        storage_efficiency = storage_eff(volume, surface_area)
        cost_efficiency = cost_eff(cost, volume)
        print(f'For {can_name:<13}:  Storage Efficiency: {storage_efficiency:.1f}  Cost Efficiency: {cost_efficiency:.5f}')
        print('--------------')
def cylinder_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def storage_eff(volume, surface_area):
    storage_efficency = volume / surface_area
    return storage_efficency

def cost_eff(cost, volume):
    cost_efficiency = cost / volume
    return cost_efficiency


main()