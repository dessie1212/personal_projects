import numpy
import pickle
import joblib
import pandas as pd

# Load the model and label encoder
model_path = '/Users/ERC/Desktop/model.pkl'
label_encoder_path = '/Users/ERC/Desktop/label_encoder.pkl'
loaded_model = joblib.load(model_path)
loaded_le = joblib.load(label_encoder_path)

# Load the exercises list
with open("exercises_list.pkl", "rb") as file:
    exercises_list = pickle.load(file)

def predict_workout_plan(
    gender: str,    # 'Male' / 'Female'
    age: int,
    actual_weight: int,
    dream_weight: int,
    bmi: float
) -> str:
    # Define a new observation as a DataFrame
    new_observation = pd.DataFrame([[gender, age, actual_weight, dream_weight, bmi]],
                                   columns=['Gender', 'Age', 'Actual Weight', 'Dream Weight', 'BMI'])

    # Use the model to predict the exercise index
    exercise_encoded, intensity, duration = loaded_model.predict(new_observation)[0]

    # Map the encoded exercise index to the human-readable exercise name
    exercise_index = int(exercise_encoded)  # Ensure it's an integer
    exercise = exercises_list[exercise_index]  # Get the exercise name

    return f"Predicted Exercise: {exercise}, Intensity: {intensity}, Duration: {duration}"

# Example usage
print(predict_workout_plan('Male', 25, 70, 60, 22.5))
