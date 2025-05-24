# Input jumlah persamaan dan variabel
n = int(input("Masukkan jumlah persamaan (2/3): "))
m = int(input("Masukkan jumlah variabel (1/2/3): "))

if n > m:
    print("SPL tidak punya solusi")
elif m>n:
    print("SPL memiliki solusi tak hingga")
else:
    print("SPL memiliki solusi tunggal")
    A = []  
    B = []  

    print("\n--- Input Koefisien dan Konstanta ---")
    for i in range(n):
        baris = []
        print(f"\nPersamaan ke-{i+1}:")
        for j in range(m):
            coef = float(input(f"  Koefisien x{j+1}: "))
            baris.append(coef)
        konst = float(input("  Masukkan konstanta: "))
        A.append(baris)
        B.append(konst)

    # Tampilkan sistem persamaan
    print("\n--- Sistem Persamaan Linear ---")
    for i in range(n):
        pers = ""
        for j in range (m):
            if j!=0:
                pers += "+"
            pers+=f"{A[i][j]}x{j+1}" 
        print(f"{pers} = {B[i]}")

    # Hitung solusi
    if m == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        if det == 0:
            print("\nDeterminan = 0, matriks tidak memiliki invers.")
        else:
            invers = [
                [ A[1][1]/det, -A[0][1]/det],
                [-A[1][0]/det,  A[0][0]/det]
            ]
            X = []
            for i in range(2):
                total = 0
                for j in range(2):
                    total += invers[i][j] * B[j]
                X.append(total)

            print("\n--- Solusi ---")
            for i in range(2):
                print(f"x{i+1} = {X[i]}")

    elif m == 3:
        a, b, c = A[0]
        d, e, f = A[1]
        g, h, i = A[2]

        det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
        if det == 0:
            print("\nDeterminan = 0, matriks tidak memiliki invers.")
        else:
            adj = [
                [ (e*i - f*h), -(d*i - f*g),  (d*h - e*g)],
                [-(b*i - c*h),  (a*i - c*g), -(a*h - b*g)],
                [ (b*f - c*e), -(a*f - c*d),  (a*e - b*d)]
            ]

            # Transpose dan bagi dengan det
            adj_T = []
            for x in range(3):
                row = []
                for y in range(3):
                    row.append(adj[y][x] / det)
                adj_T.append(row)

            X = []
            for i in range(3):
                total = 0
                for j in range(3):
                    total += adj_T[i][j] * B[j]
                X.append(total)

            print("\n--- Solusi ---")
            for i in range(3):
                print(f"x{i+1} = {X[i]}")