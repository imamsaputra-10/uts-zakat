
import pandas as pd

# Data global untuk harga beras dan harga menu
harga_beras = 50000  # Harga per kilogram beras (misalnya 50.000 Rupiah per kg)
data_zakat = []

# Fungsi untuk menampilkan harga beras
def tampilkan_harga_beras():
    print(f"Harga beras saat ini: {harga_beras} rupiah per kilogram")

# Fungsi untuk input harga menu zakat fitrah
def input_harga_menu():
    global harga_beras
    harga_beras = float(input("Masukkan harga beras per kilogram (dalam rupiah): "))
    print(f"Harga beras berhasil diupdate menjadi {harga_beras} rupiah per kilogram")
    
