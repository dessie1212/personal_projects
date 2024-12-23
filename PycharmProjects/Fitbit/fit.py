import pickle

# Load the binary model.pkl file
with open('backend/workout_routine_recommender/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Now you can use the 'model' for predictions or further analysis

