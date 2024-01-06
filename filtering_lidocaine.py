`import os
import pandas as pd

def consolidate_filtered_data(input_dir, bnf_codes):
consolidated_df = pd.DataFrame() # Create an empty DataFrame to hold consolidated data

# List all CSV files in the input directory
for file in os.listdir(input_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(input_dir, file)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Filter the data for all BNF codes in the list
        filtered_df = df[df['BNFCode'].isin(bnf_codes)]

        # Append the filtered data to the consolidated DataFrame
        consolidated_df = pd.concat([consolidated_df, filtered_df], ignore_index=True)

# Save the consolidated data in the same directory
output_file = os.path.join(input_dir, 'Consolidated_Filtered_GPData.csv')
consolidated_df.to_csv(output_file, index=False)
