import os
from docx2pdf import convert

name = "your_file_name"

input_path = os.path.join("cv", f"{name}.docx")
output_path = os.path.join("cv", f"{name}.pdf")

if os.path.exists(input_path):
    try:
        convert(input_path, output_path)
        if os.path.exists(output_path):
            print(f"{name}.pdf has length: {len(output_path)} characters")
        else:
            print(f"Conversion failed: {output_path} not found")
    except Exception as e:
        print(f"Error during conversion: {e}")
else:
    print(f"Error: {input_path} does not exist")
