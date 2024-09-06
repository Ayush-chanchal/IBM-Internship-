from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('svm_pipeline.pkl')

def get_health_suggestions(prediction):
    suggestions = {
        'Good Health': "Maintain your current lifestyle with a balanced diet, regular exercise, and good sleep habits.",
        'Cardiovascular Issue': "Consider a heart-healthy diet, regular cardiovascular exercises, reduce stress, and consult with a healthcare provider.",
        'Respiratory Issue': "Avoid exposure to pollutants, refrain from smoking, ensure regular medical check-ups, and practice breathing exercises.",
        'Chronic Sleep Deprivation': "Establish a consistent sleep schedule, reduce screen time before bed, create a comfortable sleep environment, and consider speaking with a healthcare professional.",
        'Fever or Infection': "Ensure adequate rest, maintain hydration, monitor symptoms, and consult a healthcare provider if necessary.",
        'Sedentary Lifestyle': "Incorporate more physical activity into your daily routine, take regular breaks from sitting, and consider using a fitness tracker to monitor your activity levels.",
        'Low Activity Level': "Gradually increase your physical activity, set achievable goals, and engage in activities you enjoy to stay motivated.",
        'Insufficient Physical Activity': "Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, along with muscle-strengthening exercises.",
        'Sleep Disorder': "Maintain a regular sleep routine, avoid caffeine and heavy meals before bedtime, create a relaxing bedtime ritual, and seek medical advice if sleep problems persist.",
    }
    return suggestions.get(prediction, "Consult a healthcare provider for specific advice.")

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = pd.DataFrame([data])
    input_data = input_data.reindex(columns=[
        'Resting Heart Rate', 'Average Heart Rate', 'Max Heart Rate',
        'Step Count', 'Distance Traveled', 'Calories Burned',
        'Activity Duration', 'Total Sleep Duration', 'Sleep Interruptions',
        'Blood Oxygen Levels', 'Skin Temperature'
    ], fill_value=0)
    
    prediction = model.predict(input_data)[0]
    suggestion = get_health_suggestions(prediction)
    
    return jsonify({'prediction': prediction, 'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
