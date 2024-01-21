import os
import pandas as pd

def consolidate_filtered_data(input_dir, bnf_codes, output_file):
    consolidated_df_list = []

    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            try:
                file_path = os.path.join(input_dir, file)
                df = pd.read_csv(file_path)
                filtered_df = df[df['BNFCode'].isin(bnf_codes)]
                consolidated_df_list.append(filtered_df)
            except Exception as e:
                print(f"Error processing file {file}: {e}")

    consolidated_df = pd.concat(consolidated_df_list, ignore_index=True)
    consolidated_df = map_health_boards(consolidated_df)
    consolidated_df = apply_date_conversion(consolidated_df)
    consolidated_df.to_csv(output_file, index=False)

def map_health_boards(data):
    # Mapping of 'HB' to 'Health Board'
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

    data['Health Boards'] = data['HB'].map(health_board_mapping)
    return data

def convert_period_to_full_date(period):
    year = str(period)[:4]
    month = str(period)[4:6]
    return f"01.{month}.{year}"

def apply_date_conversion(df):
    df['Full Date'] = df['Period'].apply(convert_period_to_full_date)
    return df

# Define input directory and BNF codes
bnf_codes = [
    '1502010J0AAELEL', '1502010J0BWAAEL', '0407030ACBBAAAA',
    '1502010J0BSAAEL', '1502010I0BEAAAG', '0407030ACAAAAAA'
]

input_directory = r'C:\Users\ponia\OneDrive\Desktop\LidocainePatches-after_review\GP data'
output_file_path = r'C:\Users\ponia\OneDrive\Desktop\LidocainePatches-after_review\Lidocaine_patches_after_review.csv'

consolidate_filtered_data(input_directory, bnf_codes, output_file_path)
