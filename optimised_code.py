import os
import pandas as pd

def consolidate_filtered_data(input_dir, bnf_codes):
    consolidated_df = pd.DataFrame()  # Create an empty DataFrame to hold consolidated data

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

def map_health_boards(data, file_path):
    # Mapping of 'Code HB' to 'Health Board'
    health_board_mapping = {
        '7A1': 'Betsi Cadwaladr University Health Board',
        '7A2': 'Hywel Dda University Health Board',
        '7A3': 'Abertawe Bro Morgannwg University Health Board',
        '7A4': 'Cardiff and Vale University Health Board',
        '7A5': 'Cwm Taf University Health Board',
        '7A6': 'Aneurin Bevan University Health Board',
        '7A7': 'Powys Teaching Health Board',
        'RQF': 'Velindre NHS Trust',
        'RT4': 'Welsh Ambulance Services NHS Trust'
    }

    # Adjusting for the correct column name
    data['Health Board'] = data['Code HB'].map(health_board_mapping)

    # Save the updated dataframe to a new CSV file
    data.to_csv(file_path, index=False)

def convert_period_to_full_date(period):
    year = str(period)[:4]
    month = str(period)[4:6]
    return f"01.{month}.{year}"

def apply_date_conversion(df):
    # Apply the conversion function to create a new 'date' column with full date format
    df['date'] = df['Period'].apply(convert_period_to_full_date)
    return df

# Define input directory and BNF codes (replace with actual values)
input_directory = 'path_to_input_directory'
bnf_codes = ['1502010J0AAELEL', '1502010I0BEAAAG', '1502010J0BSAAEL', '0407030ACBBAAAA']  # Replace with actual BNF codes

# Consolidate and filter data
consolidate_filtered_data(input_directory, bnf_codes)

# Load and map health boards
file_path = 'path_to_your_file.csv'  # Replace with your file path
df = pd.read_csv(file_path)
map_health_boards(df, 'updated_file_path.csv')  # Replace with new file path

# Convert period to full date and save
df = pd.read_csv('path_to_your_file.csv')  # Replace with your file path
df = apply_date_conversion(df)
df.to_csv('final_output_file_path.csv', index=False)  # Replace with final output file path
