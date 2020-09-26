"""
    Tugas penyelesaian persamaan linear.
    Metode yang ada:
        [1] Inversion
        [2] Cramer's Rule
        [3] Gauss Elimination
        [4] Gauss Jordan
"""
import numpy as np
import sys

import inversion as inv
import cramer_rule as crm
import gauss_elemination as ge
import gauss_jordan as gj

def main():
    # class instance
    inversion         = inv.Inversion()
    cramer            = crm.CramerRule()
    gauss_elimination = ge.GaussElemination()
    gauss_jordan      = gj.GaussJordan()

    # Jumlah n persamaan yang akan diselesaikan
    n = int(input('Jumlah (n) persamaan: '))

    a = np.zeros((n,n+1))
    x = np.zeros(n)

    # Memasukkan input matrix
    print("\nMasukkan input persamaan dalam bentuk matrix (mtx) %dx%d" %(n, n))
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input( 'mtx['+str(i)+']['+ str(j)+']='))

    """ RESULTS """
    # print matrix
    print("\n MATRIX PERSAMAAN")
    print(a)

    # Inversion
    inversion.inversion(n, a)

    # Cramers's Rule
    cramer.cramer_rule(n, a)

    # Gauss Elimination
    gauss_elimination.gauss_elimination(n, a, x)

    # Gauss-Jordan
    gauss_jordan.gauss_jordan(n, a, x)

if __name__ == "__main__":
    # execute only if run as a script
    main()