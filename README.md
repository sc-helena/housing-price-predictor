# House Price Predictor Model 🏠
Creates a simple linear regression model to predict housing prices in California.

![Static Badge](https://img.shields.io/badge/python-3.9%2B-brightgreen)
![Static Badge](https://img.shields.io/badge/dataset-Kaggle-blue)
![Static Badge](https://img.shields.io/badge/model-sckit--learn-orange)
![Static Badge](https://img.shields.io/badge/data--analytics-numpy-lightblue)


# Table of Contents
* Features
* Installation
* Usage
* Project Structure


# Features 
* **Data Analysis:** Clean and explore housing data using NumPy and pandas.
* **ML Model:** Train a regression model with Scikit-Learn.
* **Model Evaluation:** Track performance metrics.
* **Prediction Demo:** Test the model directly in Jupyter notebooks or via CLI (future UI planned).

## Installation

### Prequesits
* **Kaggle Account:** Register at Kaggle and [create an API-Key](https://www.kaggle.com/docs/api).
* **Python 3.9+:** Ensure Python and venv are installed.

### Setup
1. Setup a virtual environment and install packages
```
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt 

```

2. Place your Kaggle API key (kaggle.json) in ~/.kaggle/.

# Usage

- **Data Loading & Preprocessing, Model Training** (notebooks/data_loader.ipynb):
    - Load the [Kaggle dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices).
    - Preprocess data (handling missing values, feature engineering).
    - Train and save the Scikit-Learn model using [pickle](https://docs.python.org/3/library/pickle.html).
- **Model Evaluation** (notebooks/model_evaluation.ipynb):
    - Evaluate performance metrics.
- **Run Predictions** (notebooks/run_model.ipynb):
    - Test the model with custom inputs.


