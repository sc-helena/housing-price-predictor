import os
from pathlib import Path

current_path = Path(__file__)

DATASET = "camnugent/california-housing-prices"
MODEL_PATH = os.path.join(current_path.parent.parent, "model/price_estimator_model.pkl")
TRAIN_DATA_PATH = os.path.join(current_path.parent.parent, "data/strat_train_set.csv")
TEST_DATA_PATH = os.path.join(current_path.parent.parent, "data/strat_test_set.csv")
RANDOM_SEED = 3
