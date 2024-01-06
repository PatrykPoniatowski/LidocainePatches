import pandas as pd

def convert_period_to_full_date(period):
    year = str(period)[:4]
    month = str(period)[4:6]
    return f"01.{month}.{year}"

# Load the dataset from the specified path
df = pd.read_csv('Please insert here your local direct pathway')

# Apply the conversion function to create a new 'date' column with full date format
df['date'] = df['Period'].apply(convert_period_to_full_date)

# Save the updated DataFrame back to a CSV file in the same directory
output_file_path = 'Please insert here your local direct `pathway'`
