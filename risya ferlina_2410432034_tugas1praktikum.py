#daftar_barang dan harga_barang
daftar_barang = {
    "wardah liquid lip glasting " : 67490,
    "glad2glow perfect blurring powder foundation" : 71155,
    " dermacept RX moisturizing sunscreen 50g" : 95700,
    "dorskin  matcha glow dream mask moisturizing " : 60000,
    "tresemme treatment mask keratin smooth 180 ml" : 60000,
    "pantene conditioner total damage care 290 ml" : 51000,
    "vaselin gluta-hya body serum dewy radiance serum burst " : 62900,
    "handuk terry palmer signature" : 100000,
    "miniso official parfum wanita EDT cristal diamond" : 71052,
    "cetaphil moisturizing lotion 59 ml" : 57900
}
print("==================== Daftar Barang ====================")
print("1. wardah liquid lip glasting                             Rp.67.490")
print("2. glad2glow perfect blurrung powder foundation           Rp.71.155")
print("3. dermacept RX moisturizing sunscreen 50g                Rp.95.700") 
print("4. dorskin  matcha glow dream mask moisturizing           Rp.60.000")
print("5. tresemme treatment mask keratin smooth 180 ml          Rp.60.000")
print("6. pantene conditioner total damage care 290 ml           Rp.51.000")
print("7. vaselin gluta-hya body serum dewy radiance serum burst Rp.62.900")
print("8. handuk terry palmer signature                          Rp.100.000")
print("9. miniso official parfum wanita EDT cristal diamond      Rp.71.052")
print("10. cetaphil moisturizing lotion 59 ml                    Rp.57.900")
print("pembelian kurang dari Rp.1.000.000,- tidak mendapatkan diskon")
print("pembelian Rp.1.000.000 sampai Rp. 1.500.000,- mendapatkan diskon 10%")
print("pembelian lebih dari Rp.1.500.000,- mendapatkan diskon 15%")  
print("========================================================")
beli= input("pilih daftar_barang :")
harga_satuan = daftar_barang[beli]
jumlah = int(input("jumlah pesanan:"))
bayar = jumlah*daftar_barang[beli]

if bayar < 1000000 :
    diskon = bayar*0/100
    total = bayar - diskon
    jenis_diskon = "tidak mendapatkan diskon"
elif 1000000 >= bayar >= 1500000 :
    diskon = bayar*10/100
    total = bayar - diskon
    jenis_diskon = "diskon 10%"
elif bayar> 1500000 :
    diskon = bayar*15/100
    total = bayar - diskon
    jenis_diskon = "diskon 15%"
print("=========== Detail Pembayaran ==========")
print("daftar_barang yang di beli:",beli)
print("banyak yang di beli:",jumlah)
print("harga satuan:",harga_satuan)
print("banyak potongan harga:",jenis_diskon)
print("total biaya:",bayar)
print("total yang harus dibayar:",total)