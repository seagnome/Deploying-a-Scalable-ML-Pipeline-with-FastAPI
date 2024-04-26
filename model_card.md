# Model Card

## Model Details

### Developer

This model was developed by Andrew Quan for the educational course D501 (WGU)/Machine Learning DevOps (Udacity)

### Model Date

This model was developed on April 26th, 2024

### Model Version

This is version 1.0.0 of the model

### Model Type

This is a Random Forest classifier ML model that trains on the Census Bureau Income (1994) data, using hyperparameters.

### Resources

[Link to Dataset](https://archive.ics.uci.edu/dataset/20/census+income)


## Intended Use

### Primary Intended Usage
This model is primarily designed for predicting income above $50,000 (USD) per year, or less than or equal to $50,000 (USD) per year, sliced by data features.
Given the historical nature of the dataset, this model is primarily intended to provide statistical context about generalizations for each feature relevant to 1994.

## Evaluation Data

Dataset: [Extraction of 1994 Census Database](https://archive.ics.uci.edu/dataset/20/census+income), 48,842 rows x 14 Features

After pre-processing, the Evaluation ("Test") Dataset was set as 25%, resulting in 8,141 entries.

## Training Data

Dataset: [Extraction of 1994 Census Database](https://archive.ics.uci.edu/dataset/20/census+income), 48,842 rows x 14 Features

After pre-processing, the Evaluation ("Test") Dataset was set as 75%, resulting in 24,420 entries.

## Metrics

Model slice performance is recorded in slice_output.txt.

Precision: 0.7192

Recall: 0.6187

F1: 0.6652

## Ethical Considerations

Several of the categorical features (such as race and gender) may provide an avenue for legal and/or ethical abuse or discrimination if not handled holistically. 

## Caveats and Recommendations

As mentioned in the Model Details, the dataset is based on values recorded in 1994, making it severely outdated in several ways. This model would be more practically relevant with more recent data.

