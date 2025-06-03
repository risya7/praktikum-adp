def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Lihat catatan yang tersedia")
        print("2. Buat catatan baru")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            # Buka file (akan error jika file tidak ada)
            file = open('catatan.txt', 'r')
            data = file.read()
            file.close()
            
            if not data:
                print("Belum ada catatan yang tersedia.")
                continue
                
            # Proses data manual tanpa split
            catatan = []
            current_judul = ""
            current_isi = ""
            i = 0
            n = len(data)
            
            while i < n:
                # Cari judul
                if data[i:i+6] == "Judul:":
                    if current_judul:  # Simpan catatan sebelumnya
                        catatan.append((current_judul, current_isi))
                    i += 6
                    current_judul = ""
                    while i < n and data[i] != '\n':
                        current_judul += data[i]
                        i += 1
                    current_judul = current_judul.strip()
                    current_isi = ""
                    
                    # Cari isi
                    if i < n and data[i] == '\n':
                        i += 1
                        if data[i:i+4] == "Isi:":
                            i += 4
                            current_isi = ""
                            while i < n and data[i] != '\n':
                                current_isi += data[i]
                                i += 1
                            current_isi = current_isi.strip()
                else:
                    i += 1
            
            if current_judul:  # Simpan catatan terakhir
                catatan.append((current_judul, current_isi))
            
            if not catatan:
                print("Belum ada catatan yang tersedia.")
                continue
                
            print("\nDaftar Catatan Tersedia:")
            for idx in range(len(catatan)):
                print(f"{idx+1}. {catatan[idx][0]}")
            
            pilihan_judul = input("\nMasukkan nomor catatan yang ingin dilihat: ")
            if pilihan_judul.isdigit():
                idx = int(pilihan_judul) - 1
                if 0 <= idx < len(catatan):
                    print(f"\nJudul: {catatan[idx][0]}")
                    print(f"Isi: {catatan[idx][1]}")
                else:
                    print("Nomor catatan tidak valid.")
            else:
                print("Input harus berupa angka.")
                
        elif pilihan == "2":
            judul = input("Masukkan judul catatan: ")
            isi = input("Masukkan isi catatan: ")
            
            file = open('catatan.txt', 'a')
            file.write(f"Judul:{judul}\n")
            file.write(f"Isi:{isi}\n")
            file.close()
            
            print("Catatan berhasil disimpan!")
            
        elif pilihan == "3":
            print("Program selesai. Sampai jumpa!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
main()