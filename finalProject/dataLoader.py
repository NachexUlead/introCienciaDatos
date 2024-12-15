import pandas as pd


def loadData():
    fileName = input("Insert the name of the file: ")
    try:
        df = pd.read_csv(fileName)
        print(df)
        return df
    except FileNotFoundError:
        print("File not found, try again")
        return None
