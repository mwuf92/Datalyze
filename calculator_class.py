import numpy as np
class CalculatorClass:
    def __init__(self):
        pass

    def convert_units(self):
        value = float(input("Enter the value you want to convert: "))
        from_unit = input("Enter the unit of the value (g, kg, F, C, cm, m): ")
        to_unit = input("Enter the unit to convert to (g, kg, F, C, cm, m): ")
        if from_unit == 'g' and to_unit == 'kg':
            return value * 0.001
        elif from_unit == 'F' and to_unit == 'C':
            return (value - 32) * (5/9)
        elif from_unit == 'cm' and to_unit == 'm':
            return value * 0.01
        else:
            print("Invalid units")
            return None

    def find_mean(self):
        data_array = list(map(int,input("Enter the comma separated data array: ").split(',')))
        return np.mean(data_array)

    def find_variance(self):
        data_array = list(map(int,input("Enter the comma separated data array: ").split(',')))
        return np.var(data_array)

    def find_max_value_and_index(self):
        data_array = list(map(int,input("Enter the comma separated data array: ").split(',')))
        max_value = np.amax(data_array)
        max_index = np.argmax(data_array)
        return max_value, max_index

    def find_min_value_and_index(self):
        data_array = list(map(int,input("Enter the comma separated data array: ").split(',')))
        min_value = np.amin(data_array)
        min_index = np.argmin(data_array)
        return min_value, min_index
'''
    def main_menu(self):
        print("Select a function to use:")
        print("1. Convert units")
        print("2. Find mean")
        print("3. Find variance")
        print("4. Find max value and index")
        print("5. Find min value and index")
        choice = int(input())
        if choice == 1:
            result = self.convert_units()
            print("Converted value:",result)
        elif choice == 2:
            result = self.find_mean()
            print("Mean value:",result)
        elif choice == 3:
            result = self.find_variance()
            print("Variance:",result)
        elif choice == 4:
            result = self.find_max_value_and_index()
            print("Max value:",result[0],"\nMax index:",result[1])
        elif choice == 5:
            result = self.find_min_value_and_index()
            print("Min value:",result[0],"\nMin index:",result[1])
        else:
            print("Error")
           
calculator = CalculatorClass()
calculator.main_menu()'''