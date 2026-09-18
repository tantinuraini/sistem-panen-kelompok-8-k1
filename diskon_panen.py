# ===================================================
# FITUR 2: Perhitungan Diskon & Total (Dikerjakan Anggota C)
# Branch: feature-diskon
# ===================================================

def hitung_diskon_dan_total(subtotal):
    """
    Fungsi untuk menghitung persentase diskon, besarnya potongan,
    dan total bayar setelah diskon.
    - Subtotal >= Rp 500.000 -> Diskon 10%
    - Subtotal >= Rp 200.000 -> Diskon 5%
    - Kurang dari Rp 200.000 -> Diskon 0%
    """
    if subtotal >= 500000:
        persen_diskon = 10
    elif subtotal >= 200000:
        persen_diskon = 5
    else:
        persen_diskon = 0
        
    potongan = subtotal * (persen_diskon / 100)
    total_bayar = subtotal - potongan
    
    return potongan, total_bayar, persen_diskon
