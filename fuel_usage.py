def main():
    # Get an odometer value in U.S. miles from the user.
    start = int(input("Enter the first odometer reading (in miles): "))

    # Get another odometer value in U.S. miles from the user.
    end = int(input("Enter the second odometer reading (in miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    gallons = float(input("Enter the amount of fuel used (in gallons): "))

    mpg = miles_per_gallon(start, end, gallons)
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    # Round the liters per 100 km to two digits after the decimal.
    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    miles_per_gallon = (end_miles - start_miles) / amount_gallons
    return miles_per_gallon


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    liters_per_100_km = 235.15 / mpg
    return liters_per_100_km


main()