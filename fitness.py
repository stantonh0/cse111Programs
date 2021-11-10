# Import datetime so that it can be used to compute a person's age.
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender as M or F: ")
    birth = input("Enter your birthdate in YYYY-MM-DD form: ")
    height = int(input("Enter your height in inches: "))
    lb = int(input("Enter your weight in lbs: "))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index, and basal_metabolic_rate functions as needed.
    compute_age(birth)
    kg_from_lb(lb)
    cm_from_in(height)
    body_mass_index(lb, height)
    basal_metabolic_rate(gender, kg, cm, years)
    # Print the results for the user to see.
    print(f"Age: {years}")
    print(f"Weight in kg: {kg}")
    print(f"Height in cm: {cm}")
    print(f"BMI: {bmi}")
    print(f"BMR: {bmr}")


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = 0.45359237 * lb
    return kg
    


def cm_from_in(height):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = 2.54 * height
    return cm


def body_mass_index(lb, height):
    bmi = (10000 * kg)/((cm)^2)
    return bmi


def basal_metabolic_rate(gender, kg, cm, years):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender == "M":
        bmr = (88.362 + (13.397 * kg) + (4.799 * cm)) - (5.677 * years)
        return bmr
    elif gender == "F":
        bmr = (447.593 + (9.247 * kg) + (3.098 * cm)) - (4.330 * years)
        return bmr


# Call the main function so that
# this program will start executing.
main()
