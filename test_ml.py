import os

from numpy import load

import pytest

import pandas as pd

import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import load_model, train_model

project_path = "../Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data = pd.read_csv(os.path.join(project_path, "data", "census.csv"))
train, test = train_test_split(data, test_size=0.25)

# 
def test_RF_model():
    """
    # Determine if the created model is a Random Forest Classifier as expected
    """
    rf_model = load_model(os.path.join(project_path, "model", "model.pkl"))
    assert isinstance(rf_model, sklearn.ensemble._forest.RandomForestClassifier)


# 
def test_training_testing_datatype():
    """
    # Check that the training and testing datasets have the correct datatype (Dataframe)
    """
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)


# 
def test_dataset_sizes():
    """
    # Test row count for training and testing datasets against expected
    """
    assert train.shape[0] == 24420
    assert test.shape[0] == 8141
