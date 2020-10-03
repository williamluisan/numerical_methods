from math import sqrt, pow
from tabulate import tabulate

class Bisection:
    def fx(self, fx, x):
        return eval(fx)
    
    def xr(self, x0, x1, fx0, fx1):
        return x1 - ((fx1*(x1-x0))/(fx1-fx0))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
if __name__ == "__main__":
    bis = Bisection()

    print("""\nSymbols:
1. for 'power' calculation use: pow(x, y) --> x raised to the power y
2. for square root use: sqrt(x)\n
Input (equation) example:
Masukkan persamaan: pow(x, 3) + pow(x,2)*sqrt(3) - 2*x - 2*sqrt(3)

==FALSE POSITION==""")

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
        fx0 = bis.fx(fx, x0)
        fx1 = bis.fx(fx, x1)
        
        # nilai xr, fxr dan toleransi
        xr = bis.xr(x0, x1, fx0, fx1)
        fxr = bis.fx(fx, xr)
        tolerance = fx0*fxr

        result.append([i, x0, x1, fx0, fx1, xr, fxr, tolerance])

        # logika x0 dan x1
        if (fxr < 0):
            x0 = xr            
        
        if (fxr > 0):
            x1 = xr

        if (abs(tolerance) < float(format(1.0e-10, '.20f'))):
            break
    
    print(tabulate(result, headers=["Itr", "x0", "x1", "fx0", "fx1", "xr", "fxr", "(fx0*fxr)"]))
    print("\nMaka x = %.4f\n" % xr)