import sys
from finalProject.dataLoader import loadData
from finalProject.dataExplorer import dataExplorer
from finalProject.dataCleaner import dataCleaner
from finalProject.dataAnalysis import statisticalAnalysis
from finalProject.modelCreator import modelCreation

dfOriginal = None
workingData = None
model = None


def main():
    global dfOriginal, workingData, model

    while True:
        print("\n-------- MENU ---------")
        print("1. Load data")
        print("2. Data exploration")
        print("3. Data cleaning")
        print("4. Statistical analysis")
        print("5. Model creation")
        print("6. Exit")

        option = input("Select an option: ")

        if option == "1":
            dfOriginal = loadData()
        elif option == "2":
            dataExplorer(dfOriginal)
        elif option == "3":
            workingData = dataCleaner(dfOriginal)
        elif option == "4":
            statisticalAnalysis(workingData)
        elif option == "5":
            model = modelCreation(workingData)
        elif option == "6":
            print("thank you for use this program")
            sys.exit()
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
