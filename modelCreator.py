from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
)


def modelCreation(workingData):
    if workingData is None:
        print("you have to clean the data first(option 3)")
        return None

    if "Exited" not in workingData.columns:
        print("the variable 'exited' is not in the dataset")
        return None

    print("\n-------- MODEL CREATION ---------")

    x = workingData.drop("Exited", axis=1)
    y = workingData["Exited"]

    xTrain, xTest, yTrain, yTest = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    rf = RandomForestClassifier(random_state=42)
    paramGrid = {
        "n_estimators": [10, 50, 100],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }

    gridSearch = GridSearchCV(rf, paramGrid, cv=3, scoring="accuracy", n_jobs=-1)
    gridSearch.fit(xTrain, yTrain)
    bestParams = gridSearch.best_params_
    print("\nBest parameters:", bestParams)

    bestModel = RandomForestClassifier(**bestParams, random_state=42)
    bestModel.fit(xTrain, yTrain)

    yPred = bestModel.predict(xTest)
    yProba = bestModel.predict_proba(xTest)[:, 1]

    cm = confusion_matrix(yTest, yPred)
    auc = roc_auc_score(yTest, yProba)
    precision = precision_score(yTest, yPred)
    recall = recall_score(yTest, yPred)
    f1 = f1_score(yTest, yPred)

    tn, fp, fn, tp = cm.ravel()
    specificity = tn / (tn + fp)

    print("\nMatriz confusion:")
    print(cm)
    print(f"AUC: {auc:.4f}")
    print(f"Pesition: {precision:.4f}")
    print(f"Sensibility (Recall): {recall:.4f}")
    print(f"Especifity: {specificity:.4f}")
    print(f"Score F1: {f1:.4f}")

    print("\n-------- EXPLANATION OF CONFUSION MATRIX ---------")
    print("TN: customer not exiting and the model correctly predicted as 0")
    print(
        "fp: customer not exiting and the model incorrectly predicted as 1 incorrectly"
    )
    print("fn: customer exiting and the model incorrectly predicted as 0 incorrectly")
    print("tp: customer exiting and the model correctly predicted as 1")

    trainProba = bestModel.predict_proba(xTrain)[:, 1]
    aucTrain = roc_auc_score(yTrain, trainProba)
    print(f"AUC train: {aucTrain:.4f}")
    if (aucTrain - auc) > 0.1:
        print("The model is overfitting")
    else:
        print("The model is not overfitting")

    return bestModel
