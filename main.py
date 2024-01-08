import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Your local file path
file_path = r'C:\Users\ponia\OneDrive\Desktop\lidocaine plaster analysis\Updated_Lidocaine_Patches_Final.csv'

# Load the data
data = pd.read_csv(file_path)

data['date'] = pd.to_datetime(data['date'], dayfirst=True)

trend_data = data.groupby(['Health Board', 'date']).agg({'Items': 'sum', 'ActCost': 'sum', 'Quantity': 'sum'}).reset_index()

# Plotting trends over time for each health board
plt.figure(figsize=(15, 10))
sns.lineplot(x='date', y='Items', hue='Health Board', data=trend_data)
plt.title('Trend of Items Prescribed Over Time by Health Board')
plt.xlabel('Date')
plt.ylabel('Total Items Prescribed')
plt.xticks(rotation=45)
plt.legend(title='Health Board', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
