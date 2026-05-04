import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict_time(difficulty):
    return model.predict([[difficulty]])[0]
