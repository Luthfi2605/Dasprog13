import pandas as pd
import matplotlib.pyplot as plt

file_path = r"Data_Penduduk.xlsx"
df = pd.read_excel(file_path)

Profesi = df['Profesi'].value_counts()
plt.pie(Profesi, labels=Profesi.index, autopct='%1.1f%%', startangle=140)
plt.title('persentase Profesi penduduk')
plt.axis('equal')
plt.show()