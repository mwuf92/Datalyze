import pandas as pd
import numpy as np
import os

class GetDataClass:
    def __init__(self):
        self.data = None

    def read_data(self):
        file_path = input("Enter the file path: ")
        if os.path.exists(file_path):
            self.data = np.genfromtxt(file_path, delimiter=',')
            print(self.data)
        else:
            print("Invalid file path")


    def data_load_from_directory(self):
        directory_path = input("Enter the directory path: ")

        if not os.path.isdir(directory_path):
            raise ValueError(f"{directory_path} is not a valid directory path")

        # Get all the files in the directory
        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

        # Print all the files
        for i, file in enumerate(files):
            print(f"{i+1}. {file}")

        # Ask user to select file
        file_index = int(input("Select the file number you would like to open: "))

        # Check if the file index is valid
        if file_index < 1 or file_index > len(files):
            raise ValueError("Invalid file number")

        # Get the file name
        file_name = files[file_index-1]

        file_path = os.path.join(directory_path,file_name)

        # use the read_csv function from pandas to read the file
        data = pd.read_csv(file_path, delimiter=',', header=None, dtype=float)

        # convert the pandas dataframe to a numpy array
        data_array = data.to_numpy()
        print(data_array)
        return data_array
    
    def validate_data(self):
        directory_path = input("Enter the path of the directory containing the CSV files: ")
        csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

        # print the list of files to the user
        print("The following CSV files were found in the directory:")
        for i, f in enumerate(csv_files):
            print(f"{i + 1}. {f}")

        # ask the user which file they would like to open
        file_index = int(input("Enter the number of the file you would like to open and validate: ")) - 1

        # validate the data in the selected file
        file_path = os.path.join(directory_path, csv_files[file_index])
        df = pd.read_csv(file_path)

        # check for any NaN values
        if df.isnull().values.any():
            print("There are NaN values in the data.")
            return False

        # check that all columns are numerical
        if not all(df.dtypes == 'float64'):
            print("There are Decimal values in the data.")
            return True

        # if all checks pass, return True
        print("The data is valid.")
        return True
    
    