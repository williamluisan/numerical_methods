from math import sqrt, pow
from tabulate import tabulate

class Secant:
    def fx(self, fx, x):
        return eval(fx)
    
    def xr(self, x0, x1, fx0, fx1):
        return x1 - ((fx1*(x0-x1))/(fx0-fx1))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
if __name__ == "__main__":
    sct = Secant()

    print("""\nSymbols:
1. for 'power' calculation use: pow(x, y) --> x raised to the power y
2. for square root use: sqrt(x)\n
Input (equation) example:
Masukkan persamaan: pow(x, 3) + pow(x,2)*sqrt(3) - 2*x - 2*sqrt(3)

==SECANT==""")

    persamaan = input("Masukkan persamaan: ")
    fx = persamaan
    x0 = float(input("masukkan nilai awal x0 = "))
    x1 = float(input("masukkan nilai awal x1 = "))
    print("\nPersamaan yang akan dicari akarnya\nf(x) =", persamaan)
    print("Dengan nilai awal: x0=", x0, "; x1=", x1,"\n")

    i = 0
    result = []
    while 1:
        i+=1

        # nilai fx0 dan fx1
        fx0 = sct.fx(fx, x0)
        fx1 = sct.fx(fx, x1)
        
        # nilai xr, fxr dan toleransi
        xr = sct.xr(x0, x1, fx0, fx1)
        fxr = sct.fx(fx, xr)
        tolerance = fx0*fxr

        result.append([i, x0, x1, fx0, fx1, xr, fxr, tolerance])

        # logika x0 dan x1
        if (fxr < 0):
            x0 = xr            
        
        if (fxr > 0):
            x1 = xr

        if (abs(tolerance) < float(format(1.0e-10, '.20f'))):
            break
    
    print(tabulate(result, headers=["Itr", "x0", "x1", "f(x0)", "f(x1)", "xr", "f(xr)", "(f(x0)*f(xr))"]))
    print("\nMaka x = %.4f\n" % xr)