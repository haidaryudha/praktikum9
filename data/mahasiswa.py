class Mahasiswa:
    def _init_(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def _init_(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, nama_baru, jurusan_baru):
        for m in self.data:
            if m.nim == nim:
                m.nama = nama_baru
                m.jurusan = jurusan_baru
                return True
        return False

    def cari_data(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None