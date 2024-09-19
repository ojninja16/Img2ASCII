import pandas as pd
import random

# Function to generate random valid coordinates
def generate_valid_coordinates():
    lat = round(random.uniform(-90, 90), 6)
    lon = round(random.uniform(-180, 180), 6)
    return f"{lat},{lon}"

# Function to generate invalid coordinates
def generate_invalid_coordinates():
    # Randomly choose an invalid type
    invalid_type = random.choice(['invalid_lat', 'invalid_lon', 'invalid_format'])

    if invalid_type == 'invalid_lat':
        lat = round(random.uniform(-200, 200), 6)  # Latitude should be between -90 and 90
        lon = round(random.uniform(-180, 180), 6)
    elif invalid_type == 'invalid_lon':
        lat = round(random.uniform(-90, 90), 6)
        lon = round(random.uniform(-300, 300), 6)  # Longitude should be between -180 and 180
    else:  # invalid_format
        lat = round(random.uniform(-90, 90), 6)
        lon = round(random.uniform(-180, 180), 6)
        return f"{lat};{lon}"  # Invalid format with a semicolon instead of a comma

    return f"{lat},{lon}"

# Number of rows in the dataset
num_rows = 100  # Change this value as needed

# Generate random data with a mix of valid and invalid coordinates
data = {
    'id': range(1, num_rows + 1),
    'name': [f'Name_{i}' for i in range(1, num_rows + 1)],
    'age': [random.randint(18, 60) for _ in range(num_rows)],
    'coordinates': [
        generate_valid_coordinates() if random.random() > 0.2 else generate_invalid_coordinates()
        for _ in range(num_rows)
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('random_invalid_coordinates_dataset.csv', index=False)

print("CSV file with invalid coordinates generated successfully!")
