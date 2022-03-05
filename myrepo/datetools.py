""" Just some code to see pytest in action
"""

def is_leap_year(year):
    """ Returns True if the year is a leap year
    """
    if  year < 1:
        raise ValueError("Year must be >= 1. Actual: {}".format(year))

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def days_in_year(year):
    """ Returns the number of days in a year
    """
    if is_leap_year(year):
        return 366
    else:
        return 365



def main():
    print("Around 1900...")
    for year in range(1897, 1907):
        print("  Year {} -> leap year = {}".format(year, is_leap_year(year)))

    print("BCE...")
    year = -10
    print("Year {} -> leap year = {}".format(year, is_leap_year(year)))

    print("---- THE END ----")

if __name__ == "__main__":
    main()

