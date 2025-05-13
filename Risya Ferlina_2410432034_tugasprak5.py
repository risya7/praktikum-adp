no_pelanggan = []
nama_pelanggan=[]
total_belanja=[]

while True:
    print("\n=== MENU TOKO HASYA ===")
    print("1. Tambah data pelanggan")
    print("2. Hapus data pelanggan")
    print("3. Cek data pelanggan")
    print("4. keluar")
    
    pilihan= input("Pilih menu (1-4): ")

    if pilihan== "1":
        print("\n-- Tambah Data --")
        no = input("No Pelanggan: ")
        nama= input("Nama Pelanggan: ")
        total=float(input("Total Belanja: "))

        no_pelanggan.append (no)
        nama_pelanggan.append (nama)
        total_belanja.append (total)
        print("Data berhasil ditambahkan!")
    elif pilihan == "2":
        print("\n-- Hapus Data --")
        if len(no_pelanggan)== 0:
            print("Belum ada data pelanggan!")
            continue

        no = input("Masukkan No. Pelanggan:")

        for i in range (len(no_pelanggan)):
            if no_pelanggan[i]== no :
                no_pelanggan.pop (i)
                nama_pelanggan.pop(i)
                total_belanja.pop(i)
                print("Data berhasil dihapus!")
                break
        else:
            print("Pelanggan tidak ditemukan!") 
    elif pilihan=="3":
        print("\n-- Data Pelanggan --") 
        if len (no_pelanggan)==0:
            print("Belum ada data pelanggan")
        else:
            print("No. \t No Pelanggan \t Nama \t \t Total Belanja") 
            for i in range(len(no_pelanggan)):
                print(f"{i+1}\t{no_pelanggan[i]}\t\t{nama_pelanggan[i]}\t\t{total_belanja[i]}") 
    elif pilihan == "4":
        print("Terima Kasih! program selesai.") 
        break
    else:
        print("Pilihan tidak valid!")                  