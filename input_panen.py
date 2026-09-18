
# ===================================================
# FITUR 1: Input Data Panen
# Dikerjakan Anggota A
# Branch: feature-input
# ===================================================

def input_data_panen():
    """
    Fungsi untuk menerima input data transaksi panen.
    Mengembalikan data dalam bentuk dictionary.
    """
    print("=== INPUT DATA HASIL PANEN ===")

    nama_komoditas = input(
        "Masukkan nama komoditas (misal: Padi/Jagung): "
    )
    harga_per_kg = float(
        input("Masukkan harga per kg (Rp): ")
    )
    jumlah_kg = float(
        input("Masukkan jumlah panen (kg): ")
    )

    return {
        "komoditas": nama_komoditas,
        "harga_per_kg": harga_per_kg,
        "jumlah_kg": jumlah_kg
    }
