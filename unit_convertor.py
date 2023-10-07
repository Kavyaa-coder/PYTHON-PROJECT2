def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    while True:
        print("Unit Converter Menu:")
        print("1. Temperature Converter")
        print("2. Length Converter")
        print("3. Weight Converter")
        print("4. Exit")
        
        choice = input("Please select an option (1/2/3/4): ")
        
        if choice == '1':
            try:
                unit = input("Enter the unit of the input parameter(Celsius/Fahrenheit)as C or F: ").lower()
                if unit == 'c':
                    celsius = float(input("Enter temperature in Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"{celsius}°C is equal to {fahrenheit}°F.")
                elif unit == 'f':
                    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit}°F is equal to {celsius}°C.")
                else:
                    print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")
        elif choice == '2':
            try:
                unit = input("Enter the unit of the input parameter(Meters/Feet)as m or ft: ").lower()
                if unit == 'm':
                    meters = float(input("Enter length in meters: "))
                    feet = meters_to_feet(meters)
                    print(f"{meters} meters is equal to {feet} feet.")
                elif unit == 'ft':
                    feet = float(input("Enter length in feet: "))
                    meters = feet_to_meters(feet)
                    print(f"{feet} feet is equal to {meters} meters.")
                else:
                    print("Invalid unit. Please enter either 'Meters' or 'Feet'.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for length.")
        elif choice == '3':
            try:
                unit = input("Enter the unit of the input parameter (Kilograms/Pounds) as kg or lb: ").lower()
                if unit == 'kg':
                    kilograms = float(input("Enter weight in kilograms: "))
                    pounds = kilograms_to_pounds(kilograms)
                    print(f"{kilograms} kilograms is equal to {pounds} pounds.")
                elif unit == 'lb':
                    pounds = float(input("Enter weight in pounds: "))
                    kilograms = pounds_to_kilograms(pounds)
                    print(f"{pounds} pounds is equal to {kilograms} kilograms.")
                else:
                    print("Invalid unit. Please enter either 'Kilograms' or 'Pounds'.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for weight.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

        continue_program = input("Do you want to continue? (Y/N): ").upper()
        if continue_program != 'Y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
