import pandas as pd
import os

# Load datasets
exercise_groups_df = pd.read_csv('C:/Users/ERC/Desktop/Exercise groups 1.csv')
exercise_dataset_df = pd.read_csv('C:/Users/ERC/Desktop/exercise_dataset.csv')

# Base path to image folders
base_image_folder = 'C:/Users/ERC/Desktop/free-exercise-db-main/free-exercise-db-main/exercises'

# Initialize a dictionary to store exercises and their status
exercise_status = {}

# Collect all unique exercises from both datasets
exercise_list = set()

# Add exercises from exercise groups
for col in exercise_groups_df.columns[1:]:  # Skipping placeholder column if exists
    exercise_list.update(exercise_groups_df[col].dropna().astype(str).str.strip().tolist())

# Add exercises from exercise dataset
exercise_list.update(exercise_dataset_df['Exercise'].astype(str).str.strip().tolist())

# Check each exercise in the list for folder and image existence
for exercise_name in exercise_list:
    exercise_folder_path = os.path.join(base_image_folder, exercise_name)
    if os.path.exists(exercise_folder_path):
        images = []
        for img_index in range(2):  # Adjust this based on the expected number of images
            image_name = f"{img_index}.jpg"
            image_path = os.path.join(exercise_folder_path, image_name)
            if os.path.exists(image_path):
                images.append(image_path)

        # Record if images are found or not
        exercise_status[exercise_name] = images if images else ["No images found"]
    else:
        exercise_status[exercise_name] = ["Folder not found"]

# Convert results to DataFrame and save to Excel
exercise_df = pd.DataFrame(list(exercise_status.items()), columns=['Exercise', 'Image_Status'])
output_excel_path = 'C:/Users/ERC/Desktop/exercise_image_check2.xlsx'
exercise_df.to_excel(output_excel_path, index=False)

print(f"Exercise check results saved to Excel file at: {output_excel_path}")

