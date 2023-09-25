awal = (input("Masukkan teks awal:"))
akhir = input("Masukkan teks yang diganti:")

hasil = awal
for vokal in "aiueoAIUEO":
    hasil = hasil.replace(vokal, akhir)
print("teks setelah diganti:", hasil)
