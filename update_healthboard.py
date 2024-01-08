import pandas as pd

def update_health_board(file_path, output_file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Define the replacements
    replacements = {
        "ABERTAWE BRO MORGANNWG UNIVERSITY HEALTH BOARD": "SWANSEA BAY UNIVERSITY LOCAL HEALTH BOARD",
        "CWM TAF UNIVERSITY HEALTH BOARD": "CWM TAF MORGANNWG UNIVERSITY LOCAL HEALTH BOARD"
    }

    # Replace the values in the 'Health Board' column
    data['Health Board'] = data['Health Board'].replace(replacements)

    # Save the updated DataFrame to a new CSV file
    data.to_csv(output_file_path, index=False)

# Specify the file paths
input_file_path = r"C:\Users\ponia\OneDrive\Desktop\lidocaine plaster analysis\Lidocaine Patches Final.csv"
output_file_path = r"C:\Users\ponia\OneDrive\Desktop\lidocaine plaster analysis\Updated_Lidocaine_Patches_Final.csv"

# Run the function
update_health_board(input_file_path, output_file_path)

print("The Health Board column has been updated and saved to 'Updated_Lidocaine_Patches_Final.csv'")
