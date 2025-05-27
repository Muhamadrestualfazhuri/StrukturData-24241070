data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    
    daftar_nilai = []

    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))  
    for j in range(jumlah_matkul):
        matkul = input(f"  Nama mata kuliah ke-{j+1}: ")         
        nilai = float(input(f"  Nilai untuk {matkul}: "))        
        daftar_nilai.append((matkul, nilai))                     

    total_nilai = sum(nilai for _, nilai in daftar_nilai)
    rata_rata_nilai = total_nilai / jumlah_matkul if jumlah_matkul > 0 else 0

    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan,
        "daftar_nilai": daftar_nilai, 
        "nilai rata rata": rata_rata_nilai
    }

print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")

if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}, Rata rata nilai: {mhs['nilai rata rata']:.2f}")
    print("Daftar Nilai Mata Kuliah:")
    for matkul, nilai in mhs['daftar_nilai']:
        print(f"  {matkul}: {nilai:.2f}")
else:
    print("Mahasiswa tidak ditemukan.")

print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} --> {info['nama']} ({info['jurusan']}), Rata-rata nilai: {info['nilai rata rata']:.2f}")
    print("  Daftar Nilai Mata Kuliah:")
    for matkul, nilai in info['daftar_nilai']:
        print(f"    {matkul}: {nilai:.2f}")