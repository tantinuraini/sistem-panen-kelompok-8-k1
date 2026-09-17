
def input_data_panen():
    print("=== SISTEM PENCATATAN HASIL PANEN ===")
    
    komoditas = input("Masukkan nama komoditas: ")
    jumlah_kg = float(input("Masukkan jumlah hasil panen (kg): "))
    harga_per_kg = float(input("Masukkan harga per kg (Rp): "))
    
    total = jumlah_kg * harga_per_kg
    
    print("\n=== DATA HASIL PANEN ===")
    print("Komoditas       :", komoditas)
    print("Jumlah panen    :", jumlah_kg, "kg")
    print("Harga per kg    : Rp", harga_per_kg)
    print("Total biaya     : Rp", total)
    
    return komoditas, jumlah_kg, harga_per_kg, total


input_data_panen()
