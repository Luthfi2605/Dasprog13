import pandas as pd
import matplotlib.pyplot as plt

file_path = r"Data_Penduduk.xlsx"
df = pd.read_excel(file_path)

q1 = df['Penghasilan_Per_Bulan'].quantile(0.25)
q2 = df['Penghasilan_Per_Bulan'].quantile(0.50)
q3 = df['Penghasilan_Per_Bulan'].quantile(0.75)

def Kategorikan_Pendapatan(pendapatan):
    if pendapatan < q1:
        return 'Sangat rendah'
    elif q1 <= pendapatan < q2:
        return 'Rendah'
    elif q2 <= pendapatan < q3:
        return 'Menengah'
    else:
        return 'Tinggi'
    
df['Kategori_Pendapatan'] = df['Penfhasilan_Per_Bulan'].apply(Kategorikan_Pendapatan)
Kategorikan_Pendapatan  = df['Kategori_Pendapatan'].value_counts()
plt.pie(Kategorikan_Pendapatan, labels=Kategorikan_Pendapatan.index,autopct='%1.1f%%', startangle=140)
plt.title('Persentase Kategori Pendapatan Penduduk')
plt.axis('equal')
plt.show()