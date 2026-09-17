def hitung_total(jumlah_kg, harga_per_kg):
    return jumlah_kg * harga_per_kg

def hitung_diskon(total, persen_diskon):
    return total - (total * (persen_diskon / 100))

total_awal = hitung_total(100, 5000)
print("Total awal:", total_awal)
print("Total setelah diskon 10%:", hitung_diskon(total_awal, 10))
