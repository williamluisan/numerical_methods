"""
    code credit: https://www.codesansar.com/numerical-methods/gauss-jordan-method-python-program-output.htm
"""

import numpy as np
import sys
import time

class GaussJordan:
    """ fungsi menghitung eliminasi gauss
    @param    n   jumlah (n) persamaan
    @param    A   matrix persamaan 
    @param    x   matrix solusi persamaan """
    def gauss_jordan(self, n, A, x):
        start = time.time()

        # lakukan algoritma gauss-jordan
        for i in range(n):
            if A[i][i] == 0.0:
                sys.exit('Terjadi pembagian 0, exit..')
                
            for j in range(n):
                if i != j:
                    ratio = A[j][i]/A[i][i]

                    for k in range(n+1):
                        A[j][k] = A[j][k] - ratio * A[i][k]

        # kalkulasi solusi
        for i in range(n):
            x[i] = A[i][n]/A[i][i]

        end = time.time()
        calculation_time = end - start

        # tampilkan hasil
        print('\nGAUSS-JORDAN: ')
        label = 'a'
        for i in range(n):
            print(label.strip(), "= %0.2f;" %(x[i]), end = " ")
            label = chr(ord(label) + 1)
        print(" Calculation time: %0.5fs" %(calculation_time))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
# if __name__ == "__main__":
#     gauss_jordan = GaussJordan()

#     # J\jumlah n persamaan yang akan diselesaikan
#     n = int(input('Jumlah (n) persamaan: '))

#     a = np.zeros((n,n+1))
#     x = np.zeros(n)

#     # Memasukkan input matrix
#     print("\nMasukkan input persamaan dalam bentuk matrix (mtx) %dx%d" %(n, n))
#     for i in range(n):
#         for j in range(n+1):
#             a[i][j] = float(input( 'mtx['+str(i)+']['+ str(j)+']='))

#     # print matrix
#     print("\n MATRIX PERSAMAAN")
#     print(a, "\n")

#     gauss_jordan.gauss_jordan(n, a, x)
