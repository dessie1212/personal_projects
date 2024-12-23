import os
import pandas as pd

# Load the data
exercise_df = pd.read_csv('C:/Users/ERC/Desktop/exercise_dataset.csv')  # Use read_csv for CSV files
category_df = pd.read_excel('C:/Users/ERC/Desktop/exercise_images_with_paths.xlsx')

# Merge the DataFrames
merged_df = pd.merge(exercise_df, category_df, left_on='Exercise', right_on='Exercise Category', how='inner')

# Rename columns
merged_df.columns = [col.split('.')[0] if '.' in col else col for col in merged_df.columns]

# Alternatively, to rename specific columns to 'exercise types'
merged_df.rename(columns={'exercise types.1': 'exercise types', 'increasing': 'exercise types'}, inplace=True)

# Define the output directory (this should just be a directory, not a file name)
output_directory = 'C:/Users/ERC/Desktop/'

# Save the merged DataFrame to Excel
merged_df.to_excel(os.path.join(output_directory, 'combined_exercise_and_links.xlsx'), index=False)
