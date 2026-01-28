karyawan = []

print("=" * 50)
print("   PROGRAM PENGHITUNG KARYAWAN PERUSAHAAN")
print("=" * 50)
print()

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Karyawan")
    print("2. Lihat Daftar Karyawan")
    print("3. Hitung Total Karyawan")
    print("4. Hapus Karyawan")
    print("5. Keluar")
    print()
    
    pilihan = input("Masukkan pilihan (1-5): ").strip()
    
    if pilihan == '1':
        nama = input("Masukkan nama karyawan: ").strip()
        jabatan = input("Masukkan jabatan: ").strip()
        
        if nama and jabatan:
            karyawan.append(nama + " (" + jabatan + ")")
            print("Karyawan berhasil ditambahkan!")
        else:
            print("Data tidak boleh kosong!")
    
    elif pilihan == '2':
        if karyawan:
            print("\nDaftar Karyawan:")
            nomor = 1
            for k in karyawan:
                print(str(nomor) + ". " + k)
                nomor = nomor + 1
        else:
            print("Belum ada karyawan yang terdaftar.")
    
    elif pilihan == '3':
        total = 0
        for k in karyawan:
            total = total + 1
        print("\nTotal karyawan: " + str(total) + " orang")
    
    elif pilihan == '4':
        if karyawan:
            print("\nDaftar Karyawan:")
            nomor = 1
            for k in karyawan:
                print(str(nomor) + ". " + k)
                nomor = nomor + 1
            
            hapus = input("\nNomor urut karyawan yang akan dihapus: ").strip()
            try:
                index = int(hapus) - 1
                if 0 <= index < len(karyawan):
                    nama_hapus = karyawan.pop(index)
                    print("Karyawan " + nama_hapus + " berhasil dihapus!")
                else:
                    print("Nomor tidak valid!")
            except:
                print("Input tidak valid!")
        else:
            print("Belum ada karyawan yang terdaftar.")
    
    elif pilihan == '5':
        print("\nTerima kasih! Program selesai.")
        break
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")