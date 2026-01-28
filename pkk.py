# Inisialisasi list untuk menyimpan data karyawan
karyawan = []

# Tampilkan judul program
print("=" * 50)
print("   PROGRAM PENGHITUNG KARYAWAN PERUSAHAAN")
print("=" * 50)
print()

# Loop utama program
while True:
    # Tampilkan menu pilihan
    print("\nPilihan Menu:")
    print("1. Tambah Karyawan")
    print("2. Lihat Daftar Karyawan")
    print("3. Hitung Total Karyawan")
    print("4. Hapus Karyawan")
    print("5. Keluar")
    print()
    
    # Menerima input pilihan dari pengguna
    pilihan = input("Masukkan pilihan (1-5): ").strip()
    # Pilihan 1: Menambahkan data karyawan baru
    if pilihan == '1':
        # Menerima input nama dan jabatan
        nama = input("Masukkan nama karyawan: ").strip()
        jabatan = input("Masukkan jabatan: ").strip()
        
        # Validasi input tidak boleh kosong
        if nama and jabatan:
            # Tambahkan karyawan ke dalam list dengan format "Nama (Jabatan)"
            karyawan.append(nama + " (" + jabatan + ")")
            print("Karyawan berhasil ditambahkan!")
        else:
            print("Data tidak boleh kosong!")
    # Pilihan 2: Menampilkan daftar semua karyawan
    elif pilihan == '2':
        # Cek apakah ada data karyawan
        if karyawan:
            print("\nDaftar Karyawan:")
            # Tampilkan semua karyawan dengan nomor urut
            nomor = 1
            for k in karyawan:
                print(str(nomor) + ". " + k)
                nomor = nomor + 1
        else:
            print("Belum ada karyawan yang terdaftar.")
    # Pilihan 3: Menghitung total jumlah karyawan
    elif pilihan == '3':
        # Inisialisasi variabel untuk menghitung jumlah karyawan
        total = 0
        # Hitung setiap karyawan dalam list
        for k in karyawan:
            total = total + 1
        # Tampilkan total karyawan
        print("\nTotal karyawan: " + str(total) + " orang")
    # Pilihan 4: Menghapus data karyawan
    elif pilihan == '4':
        # Cek apakah ada data karyawan yang dapat dihapus
        if karyawan:
            print("\nDaftar Karyawan:")
            # Tampilkan semua karyawan dengan nomor urut
            nomor = 1
            for k in karyawan:
                print(str(nomor) + ". " + k)
                nomor = nomor + 1
            
            # Minta input nomor urut karyawan yang akan dihapus
            hapus = input("\nNomor urut karyawan yang akan dihapus: ").strip()
            try:
                # Konversi input menjadi integer dan kurangi 1 untuk index array
                index = int(hapus) - 1
                # Validasi index
                if 0 <= index < len(karyawan):
                    # Hapus karyawan dari list dan tampilkan nama yang dihapus
                    nama_hapus = karyawan.pop(index)
                    print("Karyawan " + nama_hapus + " berhasil dihapus!")
                else:
                    print("Nomor tidak valid!")
            except:
                # Tangani error jika input bukan angka
                print("Input tidak valid!")
        else:
            print("Belum ada karyawan yang terdaftar.")
    # Pilihan 5: Keluar dari program
    elif pilihan == '5':
        print("\nTerima kasih! Program selesai.")
        # Keluar dari loop while
        break
    
    # Jika pilihan tidak sesuai dengan opsi yang tersedia
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
