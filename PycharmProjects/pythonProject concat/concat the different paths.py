import pandas as pd
import ast  # For parsing string representations of lists

# Load the exercise images file
exercise_images = pd.read_excel('C:/Users/ERC/Desktop/exercise_images_with_paths.xlsx')

# Print the first few rows to see the initial format
print("Initial format of Exercise Images (first few rows):")
print(exercise_images.head())

# Function to parse the image paths column
def parse_image_paths(row):
    """Convert the image path string to a list if it's in string format."""
    if isinstance(row['Image Paths'], str):
        # Convert the string representation of the list to an actual list
        return ast.literal_eval(row['Image Paths'])
    return row['Image Paths']  # Return as is if already in list format

# Apply the parsing function to the 'Image Paths' column
exercise_images['Image Paths'] = exercise_images.apply(parse_image_paths, axis=1)

# Check the result to confirm parsing
print("\nParsed format of Exercise Images (first few rows):")
print(exercise_images.head())
