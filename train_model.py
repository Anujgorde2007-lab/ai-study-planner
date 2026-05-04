import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("dataset.csv")

X = data[["difficulty"]]
y = data["time"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully")
