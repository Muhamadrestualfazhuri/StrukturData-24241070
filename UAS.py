data_belanja = {}

nama = input("Nama custemer: ")
tanggal = input("Tanggal belanja: ")
 
belanja = []

jumlah_barang = int(input("Masukkan jumlah barang: "))  
for j in range(jumlah_barang):
        barang = input(f"  Nama barang ke-{j+1}: ")         
        harga = float(input(f"  harga satuan untuk {barang}: "))
        beli = int(input(f' jumlah beli :'))       
        harga_total = harga * beli

        data_belanja  = {
        "nama": nama,
        "tanggal belanja": tanggal,
        "barang": barang,
        "harga satuan": harga,
        "jumlah beli": beli,
    }
        belanja.append((barang, harga))    

print(f"\nNama Customer: {data_belanja['nama']}")
print(f"Tanggal Belanja: {data_belanja['tanggal belanja']}")
print(f"Jumlah Barang: {jumlah_barang}")