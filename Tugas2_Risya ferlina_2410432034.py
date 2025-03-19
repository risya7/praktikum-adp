#batas daerah
a = 1
b = 3

# jumlah partisi yang akan digunakan
n= int(input("masukkan nilai n :"))

#lebar setiap partisi (delta x)
delta_x = (b-a) / n

#menghitung luas nya
RP = 0                 # RP adalah luas daerah pada riemann 
for i in range (n):
    x_i_bar= a + (i+1) * delta_x
    f_xi_bar = x_i_bar**2 + 2*x_i_bar
    RP = RP + f_xi_bar * delta_x
print(f"luas daerah dari fungsi x^2 +2x dengan batas daerah x=1 dan x=3 dan jumlah partisi n ({n}) adalah {RP}:")