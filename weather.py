# weather.py
fahr = 32
def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels
cels = cels_from_fahr(fahr)
print(cels)