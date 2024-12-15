import numpy as np


def dataExplorer(df):
    if df is None:
        print("You hacve to load the data first(option 1)")
        return

    print("\n-------- DATA EXPLORATION ---------")
    print("First, general information about the dataset:")
    print(df.info())

    print("\nDescriptive statistics:")
    print(df.describe())

    interestColumns = ["CreditScore", "Age", "Tenure", "EstimatedSalary"]

    if all(col in df.columns for col in interestColumns):
        averages = df[interestColumns].mean()
        print("\nAverage values:")
        print("\nPromedio de CreditScore, Age, Tenure y EstimatedSalary:\n", averages)

        maxCreditScore = df["CreditScore"].max()
        maxAge = df["Age"].max()
        print("\nMaximum credit score:", maxCreditScore)
        print("\nMaximum age:", maxAge)

        secondQuarterEstimatedSalary = df["EstimatedSalary"].quantile(0.25)
        print("\nSecond quarter of EstimatedSalary:", secondQuarterEstimatedSalary)

        standardValues = df.select_dtypes(include=np.number).std()
        stdMax = standardValues.idxmax()
        print("\nColumn with highest standard deviation:", stdMax)

        correlation = df.select_dtypes(include=np.number).corr()
        correlationPair = correlation.unstack().dropna()
        correlationPair = correlationPair[
            correlationPair.index.get_level_values(0)
            != correlationPair.index.get_level_values(1)
        ]
        correlationPairSorted = correlationPair.sort_values()

        negativePair = correlationPairSorted.head(3)
        positivePair = correlationPairSorted.tail(3)

        print("\nThree variables with the highest positive correlation:")
        for (x, y), value in positivePair.items():
            print(f"{x} and {y}: {value}")
        print("\nThree variables with the highest negative correlation:")
        for (x, y), value in negativePair.items():
            print(f"{x} and {y}: {value}")

        print("\n----------- END OF DATA EXPLORATION -----------")
