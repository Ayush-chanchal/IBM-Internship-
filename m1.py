import pandas as pd


df = pd.read_csv('./large_smartwatch_health_data_with_condition.csv')  

def determine_health_condition(row):
    if row['Resting Heart Rate'] > 100 and row['Average Heart Rate'] > 120:
        return 'Cardiovascular Issue'
    elif row['Blood Oxygen Levels'] < 90:
        return 'Respiratory Issue'
    elif row['Total Sleep Duration'] < 4:
        return 'Chronic Sleep Deprivation'
    elif row['Skin Temperature'] > 37.5:
        return 'Fever or Infection'
    elif row['Step Count'] < 5000:
        return 'Sedentary Lifestyle'
    elif row['Calories Burned'] < 1500:
        return 'Low Activity Level'
    elif row['Activity Duration'] < 30:
        return 'Insufficient Physical Activity'
    elif row['Sleep Interruptions'] > 5:
        return 'Sleep Disorder'
    else:
        return 'Good Health'


df['Health Condition'] = df.apply(determine_health_condition, axis=1)

df.to_csv('upgraded_health_data.csv', index=False)

print("Updated dataset saved as 'upgraded_health_data.csv'.")
