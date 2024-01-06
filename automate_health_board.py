import pandas as pd

# Load the dataset
file_path = 'insert your file path here'

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
updated_file_path = 'insert your file path here'
data.to_csv(updated_file_path, index=False)
