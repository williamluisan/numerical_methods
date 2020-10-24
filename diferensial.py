from math import sqrt

class Diferensial:
    def P(self, x):
        return 2*x + 4*x +x
    
    def Q(self, x):
        return x + 3*x - 2*x

    def f(self, x):
        return x*3 + x**2*sqrt(3) - 2*x - 2*sqrt(3)

    # y aksen 1
    def y_1(self, fx, h):
        return (fx - fx) / 2*h

    # y aksen 2
    def y_2(self, fx, h):
        return (fx - 2*fx + fx) / h**2

if __name__ == "__main__":
    print("""
Diketahui
R(x) = y'' + P(x)y' + Q(x)y
dimana P(x) = 2*x + 4*x + x
Q(x) = x + 3*x - 2*x
dan f(x) = x*3 + x^2*sqrt(3) - 2*x - 2*sqrt(3)

hitunglah R(x).
Persamaan diatas dihitung dengan menggunakan metode "beda tengah"
""")

    diff = Diferensial()

    x = float(input("Masukkan titik tengah (x) = "))
    h = float(input("masukkan (h) = "))

    Rx = 0
    Rx = diff.y_2(diff.f(x), h) + diff.P(x) * diff.y_1(diff.f(x), h) + diff.Q(x)

    print("Dengan menggunakan metode 'beda tengah' pada persamaan diatas maka didapati R(x) = %.4f" % Rx)
