n=int(input("silahkan masukkan jumlah pendaftar:"))
i=1

for i in range (n):
    print(f"\nData pendaftar ke-{i+1}")
    Nama = str(input("Nama:"))
    Matkul = str (input("Mata kuliah Yang Diminati :"))

    while True:
        Nilai_Wawancara = float(input("Nilai Test Wawancara:"))
        if 1 <= Nilai_Wawancara <= 100:
            break
        print("Nilai harus berada pada rentang 1-100")

    while True:
        Nilai_Tulis = float(input("Nilai Test Tulis:"))
        if 1 <= Nilai_Tulis <= 100:
            break
        print("Nilai harus berada pada rentang 1- 100")

    while True:
        Nilai_Mengajar= float (input("Nilai Mengajar:"))
        if 1<= Nilai_Mengajar <= 100:
            break
        print("Nilai harus berada pada rentang 1-100")

    Rata= (Nilai_Wawancara + Nilai_Tulis + Nilai_Mengajar) / 3

    if Rata > 80:
        predikat = "Lulus"
    else:
        predikat= "Tidak lulus"
    
    print(f"{predikat}")
