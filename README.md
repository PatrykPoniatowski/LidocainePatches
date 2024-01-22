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

To replicate the automation of the whole process, please use Python code saved as filtering_lidocaine.py


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

To replicate the automation of the this process, please use Python code saved as automate_health_board.py

After cleaning the data and creating a new column here's the updated file: 
[Updated_Consolidated_Filtered_GPData - after cleaning .csv](https://github.com/PatrykPoniatowski/LidocainePatches-/files/13832459/Updated_Consolidated_Filtered_GPData.-.after.cleaning.csv)

Third Step:

I've removed the additional column 'M' – Health Board – as it was an empty column. Following that, the column 'Period' had a peculiar way of describing the period of time which was documented, e.g., 202001 – January 2020. To make it clearer for analysis, a Python script was developed to change, for example, 202001 to 01.2020.

To replicate the automation of the this process, please use Python code saved as convert_period.py

Here is a direct link to the final file: 
[Lidocaine Patches Final.csv](https://github.com/PatrykPoniatowski/LidocainePatches-/files/13832746/Lidocaine.Patches.Final.csv)

To make this process as efficient as possible, I've optimised the code and written it in one script. This script is saved as 'optimised_code.py' and, if used, needs to be adjusted to the user's needs (e.g., change of BNF codes, Health Boards, and local directorates


Update (21/1/2024 regarding BNF codes)

After reviewing all the code and all the possible resources, I've noticed significant variations in values. Consequently, I've double-checked step-by-step all the steps taken in this project to spot errors.

During an in-depth analysis, I noticed that the codes for Lidocaine patches changed after 2019; instead of 4, there are now 6 codes for Lidocaine Patches:

-1502010J0AAELEL (previous search analysis included this code) - Lidocaine 5% medicated plasters
-1502010J0BWAAEL (previous search analysis did not include this code) - Ralvo 700mg medicated plasters
-0407030ACBBAAAA (previous search analysis included this code) - Versatis 700mg medicated plasters
-1502010J0BSAAEL (previous search analysis included this code) - Versatis 700mg medicated plasters
-1502010I0BEAAAG (interestingly, this code was included in the search analysis but was not included in a different analysis performed by another user) - Lidoderm 5% patches
-0407030ACAAAAAA (previous search analysis did not include this code) - again, interestingly, a different analysis used this code, but I was unable to find a reference to this code in the BNF SNOMED code references.

Based on these conclusions, the whole code was updated and the analysis was done again 

15-22/01/2024

Based on all of the reviews, the entire code was updated. The file "Lidocaine_patches_analysis" contains all of the analysis, including the number of Lidocaine patches dispensed per 1000 people.

Since GitHub might be a challenging source of knowledge for clinicians, for the purpose of this project, I've created a Microsoft Power BI dashboard with all of the appropriate indicators, which should help in making clinical data-driven decisions.

As previously mentioned, this whole project stems from personal interest. All of the feedback is highly appreciated.
