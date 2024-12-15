import pandas as pd


def dataCleaner(dfOriginal):
    if dfOriginal is None:
        print("You have to load the data first(option 1)")
        return None

    df = dfOriginal.copy()

    print("\n-------- DATA CLEANING ---------")

    nFilasBefore = len(df)
    df = df.dropna()
    deleteRows = nFilasBefore - len(df)

    nFilasBeforeDup = len(df)
    df = df.drop_duplicates()
    duplicateRows = nFilasBeforeDup - len(df)

    deleteColumns = ["RowNumber", "CustomerId", "Surname"]
    for column in deleteColumns:
        if column in df.columns:
            df = df.drop(columns=[column], errors="ignore")

    if "Geography" in df.columns:
        df["Geography"] = df["Geography"].astype(str)
    if "Gender" in df.columns:
        df["Gender"] = df["Gender"].astype(str)

    if "Geography" in df.columns:
        df = pd.get_dummies(df, columns=["Geography"], drop_first=True)

    if "Gender" in df.columns:
        df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

    if "Exited" in df.columns:
        classCounts = df["Exited"].value_counts()
        print("\nClass distribution before cleaning:", classCounts)

        mayorityClass = classCounts.idxmax()
        minorityClass = classCounts.idxmin()
        mayorDf = df[df["Exited"] == mayorityClass]
        minorDf = df[df["Exited"] == minorityClass]

        minorDfUnsampled = minorDf.sample(len(mayorDf), replace=True, random_state=42)

        df = pd.concat([mayorDf, minorDfUnsampled], axis=0)
        print("\nClass distribution after cleaning:", df["Exited"].value_counts())

    else:
        print("\nExited column not found")

    print("\nRows deleted:", deleteRows)
    print("\nDuplicate rows deleted:", duplicateRows)
    print("\nColumns deleted:", deleteColumns)

    return df
