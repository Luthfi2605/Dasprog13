import pandas as pd
import matplotlib.pyplot as plt

file_path = r"Data_penduduk.xlsx"
df = pd.read_excel(file_path)

Pendidikan = df['Pendidikan_Terakhir'].value_counts()
Jenis_Kelamin = df['Jenis_Kelamin'].value_counts()
plt.bar(Pendidikan.index,Pendidikan.values, color ='skyblue', lebel='Pendidikan Terakhir')
plt.bar(Jenis_Kelamin.index, Jenis_Kelamin.values, color ='ligthgreen', label='Jenis Kelamin', alpha=0.7)
plt.xlabel('Pendidikan Terakhir & Jenis Kelamin')
plt.ylabel('Jumlah')
plt.title('Jumlaah Penduduk Berdasarkan Pendidikan Terakhir dan Jenis Kelamin')
plt.show()