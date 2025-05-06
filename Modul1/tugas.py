data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    nilai = int(input("masukkan nilai: "))
    nilai_2 = int(input("masukkan nilai yang lain: "))
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan,
        "nilai" : (nilai + nilai_2)/2
    }

print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")

if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}, Rata rata nilai: {mhs['nilai':]:.1f}")
else:
    print("Mahasiswa tidak ditemukan.")

print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} --> {info['nama']} ({info['jurusan']}), {info['nilai']:.1f} ")