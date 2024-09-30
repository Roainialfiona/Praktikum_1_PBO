class Barang :
    def __init__(self,nama_barang, kode_barang, jumlah_barang, kondisi_barang) :
        self.nama_barang = nama_barang
        self.kode_barang = kode_barang
        self.jumlah_barang = jumlah_barang
        self.kondisi_barang = kondisi_barang

    def informasi_Barang(self):
        print(f"Nama Barang = {self.nama_barang}")
        print(f"kode Barang = {self.kode_barang}")
        print(f"jumlah Barang = {self.jumlah_barang}")
        print(f"kondisi Barang = {self.kondisi_barang}")

Barang1 = Barang("Komputer", "KB001", "40", "Baik")
Barang2 = Barang("Proyektor", "PJ002", "1", "rusak")
Barang3 = Barang("Meja", "MJ003", "55", "Baik")

Barang1.informasi_Barang()
Barang2.informasi_Barang()
Barang3.informasi_Barang()
