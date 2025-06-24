# === Import dan Setup Awal ===
import os
import time
from termcolor import cprint, colored

nasabah_data = {}

# === Fungsi Clear Terminal ===
def clear():
    os.system("cls")

# === Animasi Loading ===
def loading(text="Memuat"):
    for i in range(3):
        print(text + "." * (i + 1))
        time.sleep(0.4)
        clear()

# === Inisialisasi File Nasabah ===
def buat_file_awal():
    with open("nasabah.txt", "a") as f:
        pass

# === #LoadNasabah - Memuat data nasabah dari file ===
def load_nasabah():
    buat_file_awal()
    with open("nasabah.txt", "r") as f:
        for line in f:
            baris = ""
            for char in line:
                if char != "\n":
                    baris += char
            pin = ""
            nama = ""
            saldo = ""
            mode = 0
            for c in baris:
                if c == ",":
                    mode += 1
                    continue
                if mode == 0:
                    pin += c
                elif mode == 1:
                    nama += c
                elif mode == 2:
                    saldo += c
            if pin:
                nasabah_data[pin] = {"nama": nama, "saldo": int(saldo)}

    # Jika file kosong, isi default
    if not nasabah_data:
        with open("nasabah.txt", "w") as f:
            f.write("1234,Rina,500000\n")
            f.write("5678,Budi,300000\n")
        load_nasabah()

# === #SaveNasabah - Menyimpan data nasabah ke file ===
def save_nasabah():
    with open("nasabah.txt", "w") as f:
        for pin in nasabah_data:
            nama = nasabah_data[pin]["nama"]
            saldo = nasabah_data[pin]["saldo"]
            f.write(pin + "," + nama + "," + str(saldo) + "\n")

# === #ValidasiAngka - Mengecek input hanya angka ===
def hanya_angka(teks):
    for karakter in teks:
        if karakter < "0" or karakter > "9":
            return False
    return True

# === #GambarATM - Tampilan awal antarmuka ATM ===
def tampilkan_gambar_atm():
    gambar_atm = """
    ╔═══════════════════════════╗
    ║       ┌───────────┐       ║
    ║       │           │       ║
    ║       │ MINI BANK │       ║
    ║       │___________│       ║
    ║  ┌─────────────────────┐  ║
    ║  │  [1] Cek Saldo      │  ║
    ║  │  [2] Setor Tunai    │  ║
    ║  │  [3] Tarik Tunai    │  ║
    ║  │  [4] Tambah Nasabah │  ║
    ║  │  [5] Hapus Nasabah  │  ║
    ║  │  [6] Logout         │  ║
    ║  └─────────────────────┘  ║
    ║        ┌────┐             ║
    ║        │ ██ │ <== Kartu   ║
    ║        └────┘             ║
    ╚═══════════════════════════╝
    """
    cprint(gambar_atm, "cyan")

# === #AnimasiKartu - Efek kartu masuk ===
def animasi_kartu_masuk():
    for i in range(3):
        clear()
        cprint("Kartu sedang dimasukkan" + "." * (i + 1), "magenta")
        time.sleep(0.5)
        clear()
    cprint("Kartu berhasil dibaca!", "green")
    time.sleep(1)

# === #AnimasiUang - Efek uang keluar ===
def animasi_uang_keluar():
    uang = ["[=    ]", "[==   ]", "[===  ]", "[==== ]", "[=====]", "💵💵💵"]
    for frame in uang:
        clear()
        cprint("Menarik Uang Tunai...", "yellow")
        print("\n" + frame)
        time.sleep(0.4)
    cprint("Silakan ambil uang Anda!", "green")
    time.sleep(1)

# === #LoginNasabah ===
def login():
    while True:
        cprint("=== LOGIN ATM ===", "cyan")
        pin = input("Masukkan PIN (4 digit): ")
        if pin in nasabah_data:
            loading("Memverifikasi")
            animasi_kartu_masuk()
            return pin
        else:
            cprint("PIN salah! Coba lagi.\n", "red")

# === #MenuUtamaNasabah ===
def menu(nasabah_pin):
    while True:
        user = nasabah_data[nasabah_pin]
        print(f"\nSelamat datang, {user['nama']}")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Tambah Nasabah Baru")
        print("5. Hapus Nasabah")
        print("6. Logout")
        pilih = input("Pilih menu: ")

        # === #CekSaldo ===
        if pilih == "1":
            cprint(f"Saldo Anda: Rp{user['saldo']}", "green")
        
        # === #SetorTunai ===
        elif pilih == "2":
            jumlah = input("Masukkan jumlah setor: ")
            if hanya_angka(jumlah):
                user["saldo"] += int(jumlah)
                cprint("Setoran berhasil!", "green")
            else:
                cprint("Input tidak valid!", "red")
        
        # === #TarikTunai ===
        elif pilih == "3":
            jumlah = input("Masukkan jumlah tarik: ")
            if hanya_angka(jumlah):
                jumlah = int(jumlah)
                if user["saldo"] >= jumlah:
                    user["saldo"] -= jumlah
                    animasi_uang_keluar()
                else:
                    cprint("Saldo tidak cukup!", "red")
            else:
                cprint("Input tidak valid!", "red")
        
        # === #TambahNasabah ===
        elif pilih == "4":
            tambah_nasabah()
        
        # === #HapusNasabah ===
        elif pilih == "5":
            hapus_nasabah()
        
        # === #LogoutNasabah ===
        elif pilih == "6":
            save_nasabah()
            loading("Keluar")
            break
        else:
            cprint("Pilihan tidak tersedia!", "red")

# === #TambahNasabahBaru ===
def tambah_nasabah():
    cprint("=== Tambah Nasabah Baru ===", "yellow")
    pin = input("PIN Baru (4 digit): ")
    if pin in nasabah_data or len(pin) != 4 or not hanya_angka(pin):
        cprint("PIN tidak valid / sudah terpakai!", "red")
        return
    nama = input("Nama: ")
    saldo = input("Saldo awal: ")
    if hanya_angka(saldo):
        nasabah_data[pin] = {"nama": nama, "saldo": int(saldo)}
        cprint("Nasabah berhasil ditambahkan!", "green")
    else:
        cprint("Saldo tidak valid!", "red")

# === #HapusNasabahByPIN ===
def hapus_nasabah():
    cprint("=== Hapus Nasabah ===", "yellow")
    pin = input("Masukkan PIN nasabah yang ingin dihapus: ")
    if pin in nasabah_data:
        del nasabah_data[pin]
        cprint(f"Nasabah dengan PIN {pin} telah dihapus.", "green")
    else:
        cprint("PIN tidak ditemukan!", "red")

# === #ProgramUtama ===
load_nasabah()
while True:
    clear()
    tampilkan_gambar_atm()
    pin_login = login()
    menu(pin_login)