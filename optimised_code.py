import os
import pandas as pd

def consolidate_filtered_data(input_dir, bnf_codes, output_file):
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

    # Add Health Board and Date columns
    consolidated_df = map_health_boards(consolidated_df)
    consolidated_df = apply_date_conversion(consolidated_df)

    # Save the consolidated data in the specified output directory
    consolidated_df.to_csv(output_file, index=False)

def map_health_boards(data):
    # Mapping of 'Code HB' to 'Health Board'
    health_board_mapping = {
        '7A1': 'Betsi Cadwaladr University Health Board',
        '7A2': 'Hywel Dda University Health Board',
        '7A3': 'Swansea Bay University Local Health Board',
        '7A4': 'Cardiff and Vale University Health Board',
        '7A5': 'Cwm Taf Morgannwg University Local Health Board',
        '7A6': 'Aneurin Bevan University Health Board',
        '7A7': 'Powys Teaching Health Board',
        'RQF': 'Velindre NHS Trust',
        'RT4': 'Welsh Ambulance Services NHS Trust'
    }

    data['HB'] = data['Health Board'].map(health_board_mapping)
    return data

def convert_period_to_full_date(period):
    year = str(period)[:4]
    month = str(period)[4:6]
    return f"01.{month}.{year}"

def apply_date_conversion(df):
    df['Full Date'] = df['Period'].apply(convert_period_to_full_date)
    return df

# Define input directory and BNF codes
input_directory = 'C:\\Users\\ponia\\OneDrive\\Desktop\\LidocainePatches\\LidocainePatches\\GP data'
bnf_codes = [
    '1502010J0AAELEL', '1502010J0BWAAEL', '0407030ACBBAAAA',
    '1502010J0BSAAEL', '1502010I0BEAAAG', '0407030ACAAAAAA'
]

# Output file path
output_file_path = 'C:\\Users\\ponia\\OneDrive\\Desktop\\LidocainePatches\\LidocainePatches\\Lidocaine_patches_after_review.csv'

# Consolidate, filter, map health boards, convert date, and save data
consolidate_filtered_data(input_directory, bnf_codes, output_file_path)
