import argparse
import os
import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

# Retrive current run's information

run = Run.get_context()
ws = run.experiment.workspace
found = False
key = "heart-disease-from-kaggle"

if key in ws.datasets.keys(): 
        found = True
        dataset = ws.datasets[key] 

# Split data into train and test set

def clean_data(data):

    x_df = data.to_pandas_dataframe().dropna()
    y_df = x_df.pop("DEATH_EVENT")
    return x_df, y_df

X, y = clean_data(dataset)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0)
    parser.add_argument('--max_iter', type=int, default=100)

    args = parser.parse_args()

    run.log("Regularization Strength: ", np.float(args.C))
    run.log("Max iterations: ", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')


if __name__ == '__main__':
    main()