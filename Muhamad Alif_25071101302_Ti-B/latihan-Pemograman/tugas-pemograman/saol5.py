# Fungsi untuk menghitung penjumlahan dan pengurangan
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

hasil_tambah, hasil_kurang = hitung(5, 3)

print(f"Penjumlahan = {hasil_tambah}")
print(f"Pengurangan = {hasil_kurang}")