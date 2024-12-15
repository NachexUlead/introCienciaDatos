import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def statisticalAnalysis(workingData):
    if workingData is None:
        print("you have to clean the data first(option 3)")
        return

    print("\n-------- STATISTICAL ANALYSIS ---------")

    numericColumns = workingData.select_dtypes(include=[np.number]).columns
    matrixCorrelation = workingData[numericColumns].corr()
    print("\nCorrelation Matrix:\n", matrixCorrelation)

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrixCorrelation, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("correlationHeatmap.jpg")
    plt.close()

    conclutions = []
    for column in numericColumns:
        if column != "Exited":
            plt.figure()
            sns.boxplot(y=workingData[column])
            plt.title(f"Distribution of {column}")
            plt.savefig(f"distribution{column}.jpg")
            plt.close()

    conclutions.append("1. Aage and creditscore has variables with atypical values")
    conclutions.append("2. the distribution of EstimatedSalary is not normal")
    conclutions.append("3. the balance presents outliers")
    conclutions.append("4. ternure present a normal distribution")
    conclutions.append("5. Age present a big dispersion")

    print("\n Conclutions based on the boxplots:\n")
    for conclusion in conclutions:
        print(conclusion)
