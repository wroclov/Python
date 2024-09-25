import zipfile
import os
import glob

def zip_files(directory_path, extensions, output_file):
    # Create a ZipFile object
    with zipfile.ZipFile(output_file, 'w') as zipf:
        for extension in extensions:
            # Search for files with the current extension in the folder and subfolders
            search_pattern = os.path.join(directory_path, f'**/*.{extension}')
            files_to_zip = glob.glob(search_pattern, recursive=True)

            if not files_to_zip:
                print(f"No files with extension .{extension} found in the folder {directory_path}")
                continue

            for file in files_to_zip:
                # Preserve folder structure by adding files with relative paths
                relative_path = os.path.relpath(file, directory_path)
                zipf.write(file, relative_path)  # Add file to zip
                print(f"Added {relative_path} to {output_file}")

    print(f"Created {output_file} successfully.")

# List of CSV file paths to merge
directory_path = r'C:\python_tmp\ZIP'
extensions = ['csv', 'txt']

# Output file path
output_file = r'C:\python_tmp\ZIP\csv.zip'

# Call the function to merge and write to the final CSV
zip_files(directory_path, extensions, output_file)