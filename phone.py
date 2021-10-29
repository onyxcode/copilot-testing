# what is the us phone number format?
def main():
    """
    This is the main function.
    """
    print("This program checks if a string is a valid US phone number.")
    print()
    number = input("Please enter a phone number: ")
    print()
    if len(number) != 12:
        print("The phone number must be 12 digits long.")
        print()
    else:
        area_code = number[:3]
        exchange = number[3:6]
        line = number[6:10]
        extension = number[10:]
        print("The phone number is", area_code, "-", exchange, "-", line, "ext", extension)
        print()
main()
