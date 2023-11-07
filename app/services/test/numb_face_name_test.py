import configparser
import os

import matplotlib.pyplot as plt

from database.database import Database

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)


def plot_face_names_histogram(face_names):
    # Count the occurrences of each face name
    face_name_counts = {name: face_names.count(name) for name in set(face_names)}

    # Set the threshold for passing
    threshold = config.getint('face_function_config', 'number_of_face_required')

    # Calculate pass and fail counts
    pass_count = len([count for count in face_name_counts.values() if count > threshold])
    fail_count = len(face_name_counts) - pass_count

    # Print the results for each face name
    pass_faces = [f"{name} ({count} times)" for name, count in face_name_counts.items() if count >= threshold]
    fail_faces = [f"{name} ({count} times)" for name, count in face_name_counts.items() if count < threshold]

    print(f"Passed faces: {', '.join(pass_faces)}")
    print(f"Failed faces: {', '.join(fail_faces)}")

    print(f"Face Pass: {pass_count}")
    print(f"Face Fail: {fail_count}")

    # Create a bar chart
    labels = list(face_name_counts.keys())
    counts = list(face_name_counts.values())

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.bar(labels, counts, color='blue')
    ax.set_xlabel('Face Names')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Face Names')
    plt.xticks(rotation=45)

    plt.show()


# Assuming you have your list of face names
db = Database()
known_face_encodings, known_face_names = db.get_image_files_and_name()
# Assuming you have queried and calculated percentages already
face_names = known_face_names  # Example list of face_names

# Call the function to plot and print results
plot_face_names_histogram(face_names)
