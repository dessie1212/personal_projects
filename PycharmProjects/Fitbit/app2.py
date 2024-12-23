
import requests
import os

import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_exercises(base_url, level):
    exercises = []
    page_number = 1

    while True:
        # Construct the URL for the current page with the level filter
        url = f"{base_url}/?level={level}&page={page_number}"
        print(f"Fetching page: {url}")

        response = requests.get(url)  # No headers
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}: {response.status_code}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract exercises from the current page
        exercise_rows = soup.find_all('div', class_='ExResult-row')
        if not exercise_rows:
            print("No more exercises found.")
            break

        for row in exercise_rows:
            name = row.find('a', itemprop='name').text.strip()
            muscle_targeted = row.find('div', class_='ExResult-muscleTargeted')
            muscle_targeted = muscle_targeted.text.strip().split(':')[-1].strip() if muscle_targeted else None
            equipment_type = row.find('div', class_='ExResult-equipmentType')
            equipment_type = equipment_type.text.strip().split(':')[-1].strip() if equipment_type else None
            rating = row.find('div', class_='ExRating-badge').text.strip()

            # Get images
            images = [img['src'] for img in row.find_all('img', class_='ExResult-img')]

            # Append the exercise data to the list
            exercises.append({
                'name': name,
                'muscle_targeted': muscle_targeted,
                'equipment_type': equipment_type,
                'rating': rating,
                'images': images,
                'level': level  # Add the level here
            })

        # Increment the page number to load more exercises
        page_number += 1

    return exercises


# Usage
base_url = "https://www.bodybuilding.com//exercises/finder"
level = "beginner"  # Change this to "intermediate" or "advanced" as needed
exercises_data = scrape_exercises(base_url, level)

'''
# Create a DataFrame
df = pd.DataFrame(exercises_data)

# Save to Excel
excel_file = f'exercises_data_{level}.xlsx'
df.to_excel(excel_file, index=False)

print(f"Total exercises found: {len(exercises_data)}")
print(f"Data saved to {excel_file}")
'''