import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import configparser
import os
from database.database import Database

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

class Plot:
    def plot_face_names_histogram(self):
        db = Database()
        _, known_face_names = db.get_image_files_and_name()

        # Assuming you have queried and calculated percentages already
        face_names = known_face_names  # Example list of face_names
        # Count the occurrences of each face name
        face_name_counts = {name: face_names.count(name) for name in set(face_names)}

        # Set the threshold for passing
        threshold = config.getint('name_recognition_config', 'number_of_face_required')

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

        fig, ax = plt.subplots(figsize=(16/2.2, 9/2.2))
        ax.bar(labels, counts, color='blue')
        # Draw a horizontal line at the threshold value
        ax.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold: {threshold}')
        ax.set_xlabel('Face Names')
        ax.set_ylabel('Frequency')
        ax.set_title('Frequency of Face Names')
        plt.xticks(rotation=45)

        # Save the plot to a BytesIO object
        img_stream = BytesIO()
        plt.savefig(img_stream, format='png', bbox_inches='tight', pad_inches=0.1)
        img_stream.seek(0)

        plt.close()  # Close the figure to free up resources

        return img_stream
