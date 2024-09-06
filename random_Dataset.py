import pandas as pd
import numpy as np

# Number of rows for the dataset
num_rows = 1000

# Generate synthetic data
data = {
    "Timestamp": pd.date_range(start='2024-01-01', periods=num_rows, freq='H'),
    "Resting Heart Rate": np.random.randint(50, 80, size=num_rows),
    "Average Heart Rate": np.random.randint(60, 100, size=num_rows),
    "Max Heart Rate": np.random.randint(90, 150, size=num_rows),
    "Step Count": np.random.randint(0, 20000, size=num_rows),
    "Distance Traveled": np.round(np.random.uniform(0, 20, size=num_rows), 2),
    "Calories Burned": np.round(np.random.uniform(0, 1000, size=num_rows), 2),
    "Activity Type": np.random.choice(["Walking", "Running", "Cycling", "Idle"], size=num_rows),
    "Activity Duration": np.random.randint(0, 120, size=num_rows),
    "Total Sleep Duration": np.round(np.random.uniform(0, 10, size=num_rows), 2),
    "Sleep Stages": np.random.choice(["Light", "Deep", "REM", "Mixed"], size=num_rows),
    "Sleep Quality": np.random.choice(["Good", "Fair", "Poor"], size=num_rows),
    "Sleep Interruptions": np.random.randint(0, 5, size=num_rows),
    "Blood Oxygen Levels": np.round(np.random.uniform(90, 100, size=num_rows), 2),
    "Skin Temperature": np.round(np.random.uniform(35, 37.5, size=num_rows), 1),
    "Accelerometer (X)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Accelerometer (Y)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Accelerometer (Z)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Gyroscope (X)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Gyroscope (Y)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Gyroscope (Z)": np.round(np.random.uniform(-1, 1, size=num_rows), 2),
    "Stress Levels": np.random.choice(["Low", "Medium", "High"], size=num_rows),
    "Mood": np.random.choice(["Happy", "Neutral", "Sad"], size=num_rows)
}

# Create DataFrame
synthetic_dataset = pd.DataFrame(data)

# Show first few rows of the synthetic dataset
synthetic_dataset.head()
