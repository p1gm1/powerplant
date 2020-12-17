# Pandas
import pandas as pd 

# utils
import joblib


class Utils:
    """Handles the utils for data"""
    def load_from_csv(self, path):
        """Load to a csv"""
        return pd.read_csv(path)

    def features_target(self, dataset, dropcols, y):
        """Slplit features and targets"""
        X = dataset.drop(dropcols, axis=1)
        y = dataset[y]
        return X, y

    def model_export(self, clf, score):
        """Export best model."""
        joblib.dump(clf, './models/best_model.pkl')