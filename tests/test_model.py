import joblib
from sklearn.metrics import accuracy_score
import pandas as pd


def test_model():
    model = joblib.load('./models/model.pkl')

    df = pd.read_csv('./tests/valid.csv')
    X_valid = df.drop(columns='quality')
    y_valid = df['quality']

    y_pred = model.predict(X_valid)

    assert accuracy_score(y_valid, y_pred) > 0.55
