import pandas as pd
import joblib


model = joblib.load('svm_pipeline.pkl')

input_data = pd.DataFrame([{
    'Resting Heart Rate': 60,
    'Average Heart Rate': 40,
    'Max Heart Rate': 60,
    'Step Count': 1000,
    'Distance Traveled': 8.0,  # in km
    'Calories Burned': 300,
    'Activity Duration': 120,  # in mins
    'Total Sleep Duration': 480,  # in mins
    'Sleep Interruptions': 2,
    'Blood Oxygen Levels': 98,
    'Skin Temperature': 36.5,  # in Celsius
    
}])

# Making predictions
predictions = model.predict(input_data)

print(f"Predicted Health Condition: {predictions[0]}")
