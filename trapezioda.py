class Trapezioda:
    def fx(self, x):
        return 0.2 + (25*x) - (200*x*2) + (675*x*3) - (900*x*4) + (400*x*5)

if __name__ == "__main__":
    print("""
Diketahui 
f(x) = 0,2 + 25x - 200x2 + 675x3 - 900x4 + 400x5
dalam interval 0 <= x <= 0,8
dengan jumlah pembagi (n) = 5
""")

    trz = Trapezioda()

    # batas atas
    a = float(input("masukkan batas bawah (a) = "))
    b = float(input("masukkan batas atas (b) = "))
    n = input("masukkan jumlah pembagi (n) = ")

    # h atau delta
    h = (b-a)/n

    # x1 (batas atas - pembagi)
    x1 = (b/n)

    I = x = 0
    I += trz.fx(a) # masukkan f(xi)
    # masukkan f(n+1)
    for i in range(n-1):
        x += x1
        if ((x < a) or (x > b)):
            print("galat !, x diluar range 0 <= x <= 0.8")
            exit()
        I += 2 * trz.fx(x)
    I += trz.fx(b) # masukkan f(n)
    I = h / 2 * (I) # kalikan I dengan h/2

    print("Hasil integral dari persamaan diatas dengan jumlah pembagi = %d" % n)
    print("adalah = %.4f" % I)