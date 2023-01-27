from data_class import GetDataClass
from calculator_class import CalculatorClass
from plot_class import PlotAndSimulate

data = GetDataClass()
calculator = CalculatorClass()
plot = PlotAndSimulate()

def main():
    while True:
        # Print a message explaining the functions in the software and what they can do.
        print("Welcome to our software! We have the following functions available:")
        print(" 1.  Load data from file(Excel file)")
        print(" 2.  Loads data from files in the directory")
        print(" 3.  Validates data (i.e. no NaN, all numbers, etc.)")
        print(" 4.  Convert units")
        print(" 5.  Find mean")
        print(" 6.  Find variance")
        print(" 7.  Find min value and index")
        print(" 8.  Find max value and index")
        print(" 9.  Simulates a random dataset")
        print("10.  Normal Plot data ")
        print("11.  Scatter Plot data")
        # Ask the user to choose one function to use.
        user_choice = input("Please enter the number of the function you would like to use: ")

        # Depending on the user's choice, ask the user for the input required to execute the function.
        if user_choice == "1":
            data.read_data()
        elif user_choice == "2":
            data.data_load_from_directory()
        elif user_choice == "3":
            data.validate_data()
        elif user_choice == "4":
            result = calculator.convert_units()
            print("Converted value:",result)
        elif user_choice == "5":
            result = calculator.find_mean()
            print("The mean value is: ", result)
        elif user_choice == "6":
            result = calculator.find_variance()
            print("The variance value is: ", result)
        elif user_choice == "7":
            result = calculator.find_min_value_and_index()
            print("The Minimum value and index are: ", result)
        elif user_choice == "8":
            result = calculator.find_max_value_and_index()
            print("The Maximum value and index are: ", result)
        elif user_choice == "9":
            result = plot.simulate_data()
            print("The Simulate Dataset is: ", result)
        elif user_choice == "10":
            result = plot.simulate_data()
            plot.plot_normal(result)
        elif user_choice == "11":
            x = plot.get_data_from_user("x")
            y = plot.get_data_from_user("y")
            plot.plot_scatter(x, y)
            
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")

        # Perform the user-defined function and print the results.
        print("Function completed.")

        # Ask the user if they would like to repeat or close the software.
        repeat = input("Would you like to repeat? (yes/no): ")
        if repeat.lower() != "yes":
            # Close the software
            print("Thank you for using our software. Goodbye!")
            break

if __name__ == "__main__":
    main()
