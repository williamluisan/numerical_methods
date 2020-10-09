from math import sqrt, pow
from tabulate import tabulate
import sympy as sym

class GnrzNewton:
    def fx(self, fx, x):
        return eval(str(fx))
    
    def xr(self, x, w, fx, dfdx):
        return x - (w * (fx/dfdx))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
if __name__ == "__main__":
    nr = GnrzNewton()

    print("""\nSymbols:
1. for 'power' calculation use: x**y --> x raised to the power y
2. for square root use: sqrt(x)\n
Input (equation) example:
Masukkan persamaan: x**3 + x**2*sqrt(3) - 2*x - 2*sqrt(3)

==GENERALIZED NEWTON==""")

    persamaan = input("Masukkan persamaan: ")
    fx   = persamaan
    dfdx = str(sym.diff(persamaan))
    x = float(input("masukkan nilai awal x0 = "))
    w = float(input("masukkan (w) Over Relaxation Factor = "))
    print("\nPersamaan yang akan dicari akarnya\nf(x) =", persamaan)
    print("df/dx =", dfdx, "\n")
    print("dengan nilai awal: x0=", x, "dan w=", w, "\n")
    
    i = 0
    result = []
    while 1:
        i+=1

        # hitung fx dan dfdx
        fx_res = nr.fx(fx, x)
        dfdx_res = nr.fx(dfdx, x)

        if (dfdx_res == 0):
            print("! berhenti: ditemukan df/dx = 0")
            break

        # nilai xr
        xr = nr.xr(x, w, fx_res, dfdx_res)

        result.append([i, x, abs(fx_res), dfdx_res, xr])
        
        if (abs(fx_res) < float(format(1.0e-10, '.20f'))):
            break
        else:
            x = xr
        
    print(tabulate(result, headers=["Itr", "x", "fx", "df/dx", "xr"]))
    print("\nMaka x = %.4f\n" % x)