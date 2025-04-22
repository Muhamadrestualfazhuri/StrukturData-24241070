mahasiswa = []

def create_data():
    """Menambahkan nama mahasiswa ke dalam list."""
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")
    mahasiswa.append(nama_mahasiswa)
    print(f"Nama '{nama_mahasiswa}' berhasil ditambahkan.")

def read_data():
    if len(mahasiswa) <=0 :
        print("Data mahasiswa belum ada")
    else:
        for indeks in range(len(mahasiswa)):
            print("[%d] %s" % (indeks, mahasiswa[indeks]))

def update_data():
    """Mengubah nama mahasiswa berdasarkan indeks."""
    read_data()
    indeks = input("Inputkan ID Mahasiswa yang ingin diubah: ")
    if indeks.isdigit():
        indeks = int(indeks)
        if 0 <= indeks < len(mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            mahasiswa[indeks] = nama_baru
            print(f"Nama mahasiswa dengan ID {indeks} berhasil diubah menjadi '{nama_baru}'.")
        else:
            print("ID Mahasiswa tidak ditemukan.")
    else:
        print("Input tidak valid. Harap masukkan angka.")

def delete_data():
    """Menghapus nama mahasiswa berdasarkan indeks."""
    read_data()
    indeks = input("Inputkan ID Mahasiswa yang ingin dihapus: ")
    if indeks.isdigit():
        indeks = int(indeks)
        if 0 <= indeks < len(mahasiswa):
            nama_terhapus = mahasiswa.pop(indeks)
            print(f"Nama '{nama_terhapus}' dengan ID {indeks} berhasil dihapus.")
        else:
            print("ID Mahasiswa tidak ditemukan.")
    else:
        print("Input tidak valid. Harap masukkan angka.")

def show_menu():
    """Menampilkan menu pilihan."""
    print("\n" + 5 * "*-", "MENU", 5 * "-*")
    print("[1] Tambah Mahasiswa")
    print("[2] Tampilkan Mahasiswa")
    print("[3] Ubah Mahasiswa")
    print("[4] Hapus Mahasiswa")
    print("[5] Keluar")
    
    menu = input("PILIH MENU: ")
    if menu.isdigit():
        return int(menu)
    else:
        print("Input tidak valid. Harap masukkan angka.")
        return None

if __name__ == "__main__":
    while True:
        pilihan = show_menu()
        if pilihan == 1:
            create_data()
        elif pilihan == 2:
            read_data()
        elif pilihan == 3:
            update_data()
        elif pilihan == 4:
            delete_data()
        elif pilihan == 5:
            print("Terima kasih! Sampai jumpa lagi.")
            exit()
        else:
            print("Pilihan anda tidak ada dalam menu.")