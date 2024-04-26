import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)
project_path = "../Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data_path = os.path.join(project_path, "data", "census.csv")
print(data_path)
data = pd.read_csv(data_path)


train, test = train_test_split(data, test_size = 0.25)
#print("Train ",train)
#print("Test ", test)

# DO NOT MODIFY
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


X_train, y_train, encoder, lb = process_data(
    # your code here
    # use the train dataset 
    # use training=True
    # do not need to pass encoder and lb as input
        train, 
        categorical_features=cat_features, 
        label="salary", 
        training=True
    )

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

model = train_model(X_train, y_train)

# save the model and the encoder
model_path = os.path.join(project_path, "model", "model.pkl")
save_model(model, model_path)
encoder_path = os.path.join(project_path, "model", "encoder.pkl")
save_model(encoder, encoder_path)

# load the model
model = load_model(
    model_path
) 

preds = inference(model, X_test)

# Calculate and print the metrics
p, r, fb = compute_model_metrics(y_test, preds)
print(f"Precision: {p:.4f} | Recall: {r:.4f} | F1: {fb:.4f}")


for col in cat_features:
    # iterate through the unique values in one categorical feature
    for slicevalue in sorted(test[col].unique()):
        count = test[test[col] == slicevalue].shape[0]
        p, r, fb = performance_on_categorical_slice(
            # your code here
            # use test, col and slicevalue as part of the input
            test,
            col,
            slicevalue,
            cat_features,
            label="salary",
            encoder=encoder,
            lb=lb,
            model=model
        )
        with open("slice_output.txt", "a") as f:
        	print(f"{col}: {slicevalue}, Count: {count:,}", file=f)
        	print(f"Precision: {p:.4f} | Recall: {r:.4f} | F1: {fb:.4f}", file=f)

