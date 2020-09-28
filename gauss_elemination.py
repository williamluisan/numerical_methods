"""
    code credit: https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm
"""

import numpy as np
import sys
import time

class GaussElemination:
    """ fungsi menghitung eliminasi gauss
    @param    n   jumlah (n) persamaan
    @param    A   matrix persamaan 
    @param    x   matrix solusi persamaan """
    def gauss_elimination(self, n, A, x):
        start = time.time()

        # lakukan Gauss Elimination
        for i in range(n):
            if A[i][i] == 0.0:
                sys.exit('Terjadi pembagian 0, exit..')
                
            for j in range(i+1, n):
                ratio = A[j][i]/A[i][i]
                
                for k in range(n+1):
                    A[j][k] = A[j][k] - ratio * A[i][k]

        # subtitusi
        x[n-1] = A[n-1][n]/A[n-1][n-1]
        for i in range(n-2,-1,-1):
            x[i] = A[i][n]
            
            for j in range(i+1,n):
                x[i] = x[i] - A[i][j]*x[j]
            
            x[i] = x[i]/A[i][i]
        
        end = time.time()
        calculation_time = end - start

        # tampilkan hasil
        print('\nELIMINASI GAUSS: ')
        label = 'a'
        for i in range(n):
            print(label.strip(), "= %0.2f;" %(x[i]), end = " ")
            label = chr(ord(label) + 1)
        print(" Calculation time: %0.5fs" %(calculation_time))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
# if __name__ == "__main__":
#     gauss = GaussElemination()

#     # jumlah n persamaan yang akan diselesaikan
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

#     gauss.gauss_elimination(n, a, x)