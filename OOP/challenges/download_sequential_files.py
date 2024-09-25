import requests
import os

def download_files(url_template, output_directory, num_images):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i in range(1, num_images + 1):  # Loop through the sequence of images
        # Generate the file name based on the index
        file_name = f"image{str(i).zfill(3)}.jpg"  # zfill pads the number with zeros
        file_url = url_template.format(str(i).zfill(3))  # Use the template to fill in the number

        print(file_url)
        # Create the full output file path
        output_file_path = os.path.join(output_directory, file_name)

        # Send the HTTP request to download the image
        response = requests.get(file_url, stream=True)

        if response.status_code == 200:
            # Write the content to a .jpg file
            with open(output_file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download {file_name}. HTTP Status Code: {response.status_code}")


# Example usage:

# The base URL with a placeholder `{}` for the sequential number
url_template = 'http://699340.youcanlearnit.net/image{}.jpg'

# Output directory for saving images
output_directory = r'C:\python_tmp\ZIP'

# Number of images to download
num_images = 10

# Start downloading images
download_files(url_template, output_directory, num_images)
