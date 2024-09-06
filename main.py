import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib

data = pd.read_csv('./upgraded_health_data.csv')
input_columns = [
    'Resting Heart Rate', 'Average Heart Rate', 'Max Heart Rate', 'Step Count',
    'Distance Traveled', 'Calories Burned', 'Activity Duration', 'Total Sleep Duration',
    'Sleep Interruptions', 'Blood Oxygen Levels', 'Skin Temperature'
]
target_column = 'Health Condition'
X = data[input_columns]
y = data[target_column]
# categorical columns are removed
numerical_columns = input_columns
# Preprocessing data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_columns)
    ]
)
# SVM model pipeline
svm_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', SVC(kernel='linear', random_state=42))
])

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training 
svm_pipeline.fit(X_train, y_train)

# Making predictions
y_pred = svm_pipeline.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy*100}%")
print("Classification Report:\n", classification_rep)

# joblib.dump(svm_pipeline, 'svm_pipeline.pkl')
