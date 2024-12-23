import requests
import json
'''
# Replace with your actual access token
access_token = 'https://api.fitbit.com/oauth2/token'

def fetch_user_profile(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    url = 'https://api.fitbit.com/1/user/-/profile.json'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Example usage
profile_data = fetch_user_profile(access_token)

# Pretty print the JSON data
print("User Profile Data:")
print(json.dumps(profile_data, indent=4))



import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.fitbit.com/oauth2/token'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'code': 'AUTHORIZATION_CODE',
    'redirect_uri': 'YOUR_REDIRECT_URI'
}
response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET'))
print(response.json())


import zipfile
import os

# Set the path to the downloaded zip file and destination folder
zip_file_path = '/path/to/dest/exercise-data-analysis.zip'
dest_folder = '/path/to/dest/'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(dest_folder)



import requests
from bs4 import BeautifulSoup

url = 'https://www.bodybuilding.com/exercises/finder/?'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all exercise containers on the page
exercises = soup.find_all('div', class_='ExResult-cell')

for exercise in exercises:
    name = exercise.find('h3').text.strip()
    muscle_group = exercise.find('div', class_='ExResult-muscleTargeted').text.strip()
    difficulty = exercise.find('div', class_='ExResult-difficulty').text.strip()

    # Extract equipment type if available
    equipment = exercise.find('div', class_='ExResult-equipmentType')
    equipment_type = equipment.text.strip() if equipment else 'Bodyweight'

    # Extract rating if available
    rating_tag = exercise.find('div', class_='ExRating')
    rating = rating_tag.text.strip() if rating_tag else 'No rating'

    print(
        f'Name: {name}, Muscle: {muscle_group}, Difficulty: {difficulty}, Equipment: {equipment_type}, Rating: {rating}')

import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.bodybuilding.com/exercises/finder/?muscle=chest'  # Replace with the actual URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

exercises = []

# Select all exercise containers (adjust the parent selector if needed)
exercise_cells = soup.select('.ExResult-cell--nameEtc')

for exercise in exercise_cells:
    try:
        # Extract name
        name = exercise.select_one('.ExHeading a').text.strip() if exercise.select_one('.ExHeading a') else 'N/A'

        # Extract muscle targeted, equipment type, and rating within the same parent div
        muscle_targeted = exercise.select_one('.ExResult-muscleTargeted a').text.strip() if exercise.select_one(
            '.ExResult-muscleTargeted a') else 'N/A'
        equipment_type = exercise.select_one('.ExResult-equipmentType a').text.strip() if exercise.select_one(
            '.ExResult-equipmentType a') else 'N/A'

        # Get rating, look for a sibling or within the current structure
        rating_container = exercise.find_next('div', class_='ExResult-cell--rating')  # Adjust if needed
        rating = rating_container.select_one(
            '.ExRating-badge').text.strip() if rating_container and rating_container.select_one(
            '.ExRating-badge') else 'N/A'

        # Add the extracted exercise data to the list
        exercises.append({
            'name': name,
            'muscle_targeted': muscle_targeted,
            'equipment_type': equipment_type,
            'rating': rating,
        })

    except Exception as e:
        print(f"Error processing exercise: {e}")
        continue  # Skip to the next exercise if any error occurs

# Display extracted exercises
for exercise in exercises:
    print(exercise)

'''
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.bodybuilding.com/exercises/finder/?muscle=chest'  # Replace with the actual URL
exercises = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Select all exercise containers
    exercise_cells = soup.select('.ExResult-cell--nameEtc')

    for exercise in exercise_cells:
        name = exercise.select_one('.ExHeading a').text.strip()
        muscle_targeted = exercise.find_next('div', class_='ExResult-cell--nameEtc').select_one(
            '.ExResult-muscleTargeted a').text.strip()
        equipment_type = exercise.find_next('div', class_='ExResult-cell--nameEtc').select_one(
            '.ExResult-equipmentType a').text.strip()
        rating = exercise.find_next('div', class_='ExResult-cell--rating').select_one(
            '.ExRating-badge').text.strip()

        # Extracting image URL
        image_element = exercise.find_previous('div', class_='ExResult-cell ExResult-cell--image')
        image_url = image_element.find('img')['src'] if image_element else None

        exercises.append({
            'name': name,
            'muscle_targeted': muscle_targeted,
            'equipment_type': equipment_type,
            'rating': rating,
            'image_url': image_url,  # Adding the image URL
        })

    # Find the next page link
    next_page = soup.select_one('a.next')  # Adjust based on actual HTML structure
    url = next_page['href'] if next_page else None

# Display extracted exercises with images
for exercise in exercises:
    print(exercise)
'''
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.bodybuilding.com/exercises/finder/?'  # Replace with the actual URL
exercises = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Select all exercise containers
    exercise_cells = soup.select('.ExResult-cell--nameEtc')

    for exercise in exercise_cells:
        # Extracting the exercise name
        name = exercise.select_one('.ExHeading a').text.strip()

        # Initialize variables
        muscle_targeted = None
        equipment_type = None
        rating = None
        image_url = None

        # Navigate to the next sibling to get muscle targeted
        muscle_div = exercise.find_next('div', class_='ExResult-details ExResult-muscleTargeted')
        if muscle_div:
            muscle_targeted = muscle_div.select_one('a').text.strip() if muscle_div.select_one('a') else None

        # Navigate to the next sibling to get equipment type
        equipment_div = exercise.find_next('div', class_='ExResult-details ExResult-equipmentType')
        if equipment_div:
            equipment_type = equipment_div.select_one('a').text.strip() if equipment_div.select_one('a') else None

        # Extracting the rating
        rating_div = exercise.find_next('div', class_='ExResult-cell--rating')
        if rating_div:
            rating = rating_div.select_one('.ExRating-badge').text.strip() if rating_div.select_one(
                '.ExRating-badge') else None

        # Extracting image URL
        image_element = exercise.find_previous('div', class_='ExResult-cell ExResult-cell--image')
        if image_element and image_element.find('img'):
            image_url = image_element.find('img')['src']

        # Append the extracted information to the list
        exercises.append({
            'name': name,
            'muscle_targeted': muscle_targeted,
            'equipment_type': equipment_type,
            'rating': rating,
            'image_url': image_url,
        })

    # Find the next page link
    next_page = soup.select_one('a.next')  # Adjust based on actual HTML structure
    url = next_page['href'] if next_page else None

# Display extracted exercises
for exercise in exercises:
    print(exercise)
'''
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.bodybuilding.com/exercises/finder/'  # Replace with the actual URL
exercises = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Select all exercise containers
    exercise_cells = soup.select('.ExResult-row')

    # Debugging: Check if exercise cells are found
    if not exercise_cells:
        print("No exercise cells found. Check the selector or page structure.")
        break

    for exercise in exercise_cells:
        # Extracting the exercise name
        name = exercise.select_one('.ExHeading a').text.strip()

        # Initialize variables
        muscle_targeted = None
        equipment_type = None
        rating = None
        images = []  # List to store image URLs

        # Extracting muscle targeted
        muscle_div = exercise.select_one('.ExResult-muscleTargeted')
        if muscle_div:
            muscle_targeted = muscle_div.select_one('a').text.strip() if muscle_div.select_one('a') else None

        # Extracting equipment type
        equipment_div = exercise.select_one('.ExResult-equipmentType')
        if equipment_div:
            equipment_type = equipment_div.select_one('a').text.strip() if equipment_div.select_one('a') else None

        # Extracting rating
        rating_div = exercise.select_one('.ExResult-cell--rating .ExRating-badge')
        if rating_div:
            rating = rating_div.text.strip() if rating_div else None

        # Extracting all image URLs
        image_cells = exercise.select('.ExResult-cell--imgs img')
        for img in image_cells:
            img_src = img['src']  # Extract the 'src' attribute
            images.append(img_src)

        # Append the extracted information to the list
        exercises.append({
            'name': name,
            'muscle_targeted': muscle_targeted,
            'equipment_type': equipment_type,
            'rating': rating,
            'images': images,  # Store list of images
        })

    # Debugging: Print number of exercises found on the page
    print(f"Found {len(exercise_cells)} exercises on the current page.")

    # Find the next page link
    next_page = soup.select_one('a.next')  # Adjust based on actual HTML structure
    if next_page and 'href' in next_page.attrs:
        url = next_page['href']  # Use relative link for the next page
        # If it's a relative URL, prepend the base URL
        url = f"https://www.bodybuilding.com/exercises/finder/{url}"  # Adjust the base URL as necessary
    else:
        print("No next page found. Ending scraping.")
        url = None

# Display extracted exercises
for exercise in exercises:
    print(exercise)
'''

import requests
from bs4 import BeautifulSoup


def scrape_exercises(base_url):
    exercises = []
    page_number = 1

    while True:
        # Construct the URL for the current page
        url = f"{base_url}/exercises/finder/{page_number}/?"
        print(f"Fetching page: {url}")

        response = requests.get(url)
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
                'images': images
            })

        # Increment the page number to load more exercises
        page_number += 1

    return exercises


# Usage
base_url = "https://www.bodybuilding.com/"
exercises_data = scrape_exercises(base_url)
print(f"Total exercises found: {len(exercises_data)}")
for exercise in exercises_data:
    print(exercise)
