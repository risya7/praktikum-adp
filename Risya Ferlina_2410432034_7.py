def hitung_tagihan(kwh, golongan):
    tarif_awal = [1500, 2500, 4000, 5000]
    tarif_lanjutan = [2000, 3000, 5000, 7000]

    if golongan < 1 or golongan > 4:
        golongan = 3

    index = golongan - 1

    if kwh <= 100:
        tagihan = kwh * tarif_awal[index]
    else:
        tagihan = 100 * tarif_awal[index] + (kwh - 100) * tarif_lanjutan[index]

    return tagihan

def main():
    kwh = int(input("Masukkan pemakaian kWh: "))
    gol_input = input("Masukkan golongan (1-4), tekan Enter untuk default golongan 3: ")

    if gol_input == "":
        golongan = 3
    else:
        golongan = int(gol_input)

    tagihan = hitung_tagihan(kwh, golongan)
    print("Total tagihan: Rp", tagihan)

main()