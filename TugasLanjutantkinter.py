import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk melakukan prediksi prodi berdasarkan nilai
def prediksi_prodi(nama, biologi, fisika, inggris):
    nilai_biologi = int(biologi.get())
    nilai_fisika = int(fisika.get())
    nilai_inggris = int(inggris.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        return "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        return "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        return "Bahasa"
    else:
        return "Tidak Dapat Diprediksi"

# Fungsi untuk menyimpan data ke SQLite
def simpan_data(nama, biologi, fisika, inggris, prediksi):
    conn = sqlite3.connect('prediksiFK.db')
    cursor = conn.cursor()

    # Buat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    # Masukkan data ke tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (Nama_siswa, Biologi, Fisika, Inggris, Prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama.get(), int(biologi.get()), int(fisika.get()), int(inggris.get()), prediksi))

    conn.commit()
    conn.close()

    messagebox.showinfo("Info", "Data berhasil disimpan!!")

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi(nama, biologi, fisika, inggris, result_label):
    prediksi = prediksi_prodi(nama, biologi, fisika, inggris)
    result_label.config(text="Hasil Prediksi: " + prediksi)

    # Simpan data ke SQLite
    simpan_data(nama, biologi, fisika, inggris, prediksi)

# Membuat GUI
root = tk.Tk()
root.title("Prediksi Prodi Pilihan")

# Label judul
judul_label = tk.Label(root, text="Ayo Lihat Potensimu", font=("Times New Roman", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entry untuk input nilai mata pelajaran
nama_label = tk.Label(root, text="Nama Siswa:")
nama_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
nama_entry = tk.Entry(root, width=30)  
nama_entry.grid(row=1, column=1, padx=10, pady=5)

biologi_label = tk.Label(root, text="Biologi:")
biologi_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
biologi_entry = tk.Entry(root, width=30)
biologi_entry.grid(row=2, column=1, padx=10, pady=5)

fisika_label = tk.Label(root, text="Fisika:")
fisika_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
fisika_entry = tk.Entry(root, width=30) 
fisika_entry.grid(row=3, column=1, padx=10, pady=5)

inggris_label = tk.Label(root, text="Inggris:")
inggris_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
inggris_entry = tk.Entry(root, width=30) 
inggris_entry.grid(row=4, column=1, padx=10, pady=5)


# Label luaran hasil prediksi
result_label = tk.Label(root, text="Hasil Prediksi: ", font=("Calibri", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Button untuk hasil prediksi
prediksi_button = tk.Button(root, text="Submit", command=lambda: hasil_prediksi(nama_entry, biologi_entry, fisika_entry, inggris_entry, result_label))
prediksi_button.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()