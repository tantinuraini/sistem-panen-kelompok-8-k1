# ===================================================
# FITUR 3: Cetak Laporan Panen (Dikerjakan Anggota B)
# Branch: feature-laporan
# ===================================================

def tampilkan_laporan_panen(data_panen, potongan, total_bayar, persen_diskon):
    """
    Fungsi untuk mencetak laporan ringkasan transaksi hasil panen.
    """
    subtotal = data_panen["harga_per_kg"] * data_panen["jumlah_kg"]
    
    print("\n" + "=" * 45)
    print("        STRUK LAPORAN TRANSAKSI PANEN        ")
    print("=" * 45)
    print(f"Nama Komoditas : {data_panen['komoditas']}")
    print(f"Harga per kg   : Rp {data_panen['harga_per_kg']:,.0f}")
    print(f"Jumlah Panen   : {data_panen['jumlah_kg']} kg")
    print("-" * 45)
    print(f"Subtotal       : Rp {subtotal:,.0f}")
    print(f"Diskon ({persen_diskon}%)    : Rp {potongan:,.0f}")
    print("=" * 45)
    print(f"TOTAL BAYAR    : Rp {total_bayar:,.0f}")
    print("=" * 45 + "\n")
