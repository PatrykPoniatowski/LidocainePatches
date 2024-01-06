**This project stems from a personal interest in the data analysis of prescribing in Wales, particularly in how the implementation of new policies and guidelines has affected lidocaine prescribing levels in Wales.**

Based on changes to the guidelines regarding lidocaine prescribing, a data analysis of lidocaine patch prescriptions was conducted. This analysis utilised data from the North Wales Shared Services Partnership (NWSSP) - [NWSSP website](https://nwssp.nhs.wales/ourservices/primary-care-services/general-information/data-and-publications/prescribing-data-extracts/general-practice-prescribing-data-extract/).

The data concerning lidocaine patches were retrieved using the BNF coding for lidocaine patches:

BNF codes for lidocaine patches for data from 2020 until 2023 were taken from the SNOMED - BNF mapping document published in October 2023 - direct link to the source - [SNOMED - BNF Mapping data](https://www.nhsbsa.nhs.uk/sites/default/files/2023-12/BNF%20Snomed%20Mapping%20data%2020231215.zip).

- 1502010J0AAELEL | Lidocaine 5% medicated plasters
- 1502010I0BEAAAG | Lidoderm 5% patches
- 1502010J0BSAAEL | Versatis 700mg medicated plasters
- and a BNF code: 0407030ACBBAAAA, which appeared in the data from 2018 and 2019.

First step:
Retrieving all the data about prescribing lidocaine patches and saving it into one file.

To automate the whole process after saving all of the 67 files, a Python script was written which helped to retrieve (based on the BNF code) all the data about lidocaine patch prescribing from 2018 until 2023 and save it in one file (attached to the project).

To replicate the automation of the whole process, please use this Python code (this code is also saved as filtering_lidocaine.py)

import os
import pandas as pd

def consolidate_filtered_data(input_dir, bnf_codes):
    consolidated_df = pd.DataFrame()  # Create an empty DataFrame to hold consolidated data

    List all CSV files in the input directory
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

# Define the input directory
input_directory = Please insert here your direct pathway 

# List of BNF codes
bnf_codes = ['1502010J0AAELEL', '1502010I0BEAAAG', '1502010J0BSAAEL', '0407030ACBBAAAA']

# Run the function
consolidate_filtered_data(input_directory, bnf_codes)


Direct link to the document - 
[Consolidated_Filtered_GPData.csv](https://github.com/PatrykPoniatowski/LidocainePatches-/files/13831423/Consolidated_Filtered_GPData.csv)


Second Step – Clarifying the Codes and Allocating Them to Particular Health Boards

Appropriate references were found on the [ONS Geoportal website](https://geoportal.statistics.gov.uk/maps/ons::local-health-boards-april-2019-names-and-codes-in-wales-1), which helps to align each Health Board with its appropriate code:

-7A1: Betsi Cadwaladr University Health Board
-7A2: Hywel Dda University Health Board
-7A3: Abertawe Bro Morgannwg University Health Board
-7A4: Cardiff and Vale University Health Board
-7A5: Cwm Taf University Health Board
-7A6: Aneurin Bevan University Health Board
-7A7: Powys Teaching Health Board
-RQF: Velindre NHS Trust
-RT4: Welsh Ambulance Services NHS Trust
I have conducted a search to determine whether the codes have changed in line with changes to the borders of Health Boards in the last five years. To my knowledge, the codes have remained the same during this period.

Furthermore, while cleaning the data, I noticed that data from April 2018 was misplaced. I have corrected this by moving it from column 'M' to column 'A' and assigning it to the correct values.

To make the analysis clearer, the column 'HB' was renamed 'HB Code'. Based on the codes listed, a new column called 'Health Board' was created, containing the name of the respective Health Board.

Here is the full Python code to replicate this step (futhermore this step is also saved as automate_health_board.py) 

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
`

After cleaning the data and creating a new column here's the updated file: 
[Updated_Consolidated_Filtered_GPData - after cleaning .csv](https://github.com/PatrykPoniatowski/LidocainePatches-/files/13832459/Updated_Consolidated_Filtered_GPData.-.after.cleaning.csv)

Third Step:

I've removed the additional column 'M' – Health Board – as it was an empty column. Following that, the column 'Period' had a peculiar way of describing the period of time which was documented, e.g., 202001 – January 2020. To make it clearer for analysis, a Python script was developed to change, for example, 202001 to 01.2020.

To replicate the whole process, here is the full Python code for this step (also this step is saved as convert_period.py)
`import` pandas as pd

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

Here is a direct link to the final file: 
[Lidocaine Patches Final.csv](https://github.com/PatrykPoniatowski/LidocainePatches-/files/13832746/Lidocaine.Patches.Final.csv)

To make this process as efficient as possible, I've optimised the code and written it in one script. This script is saved as 'optimised_code.py' and, if used, needs to be adjusted to the user's needs (e.g., change of BNF codes, Health Boards, and local directorates



