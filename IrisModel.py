#Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset (place IRIS.csv in same folder)
iris = pd.read_csv("IRIS.csv")

# Assign column names
iris.columns = ['Petal_length', 'Petal_breath', 'Sepal_length', 'Sepal_breath', 'Flower_type']

# Split data
X = iris.drop('Flower_type', axis=1)
y = iris['Flower_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=24)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'iris_model.pkl')

print("Model saved successfully!")
