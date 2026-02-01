# Program menampilkan bilangan 1-10 dan menghitung jumlahnya

# Inisialisasi variabel untuk menyimpan jumlah
jumlah = 0

for i in range(1, 11):
    print(i)
    jumlah += i

print(f"Jumlah = {jumlah}")