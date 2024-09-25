import pandas as pd



def merge_csv_files(input_files, output_file):
    # Create an empty list to hold dataframes
    dataframes = []

    # Read each CSV file and append it to the list of dataframes
    for file in input_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    # Concatenate all dataframes, join='outer' will include all columns and fill missing values with NaN
    merged_df = pd.concat(dataframes, ignore_index=True, join='outer')

    # Write the merged dataframe to the final CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV written to {output_file}")


# List of CSV file paths to merge
input_files = [r'C:\python_tmp\3.csv', r'C:\python_tmp\4.csv']

# Output file path
output_file = r'C:\python_tmp\output_unequal_pandas.csv'

# Call the function to merge and write to the final CSV
merge_csv_files(input_files, output_file)
