from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def main():
    data_mhs = DataMahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mhs.tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            data_mhs.hapus_mahasiswa(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            jurusan_baru = input("Masukkan jurusan baru (kosongkan jika tidak diubah): ")
            data_mhs.ubah_mahasiswa(nim, nama_baru, jurusan_baru)
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
            mahasiswa = data_mhs.cari_mahasiswa(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            ViewMahasiswa.tampilkan_list(data_mhs.tampilkan_semua())
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if _name_ == "_main_":
    main()