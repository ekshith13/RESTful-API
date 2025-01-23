from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import joblib

def train_model(data):
    # Preprocess the data
    X = data.drop(columns=['Downtime_Flag'])
    y = data['Downtime_Flag']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }

    # Save the model
    joblib.dump(model, 'model.pkl')
    return model, metrics

def make_prediction(model, input_data):
    # Convert input JSON to DataFrame
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    confidence = model.predict_proba(input_df).max()
    return {"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": round(confidence, 2)}
