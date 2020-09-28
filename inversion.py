import numpy as np
import sys
import time

class Inversion:
    def inversion(self, n, A):
        matrix1 = np.zeros((n, n))
        matrix2 = np.zeros(n)

        start = time.time()

        # matrix 1
        for i in range(n):
            for j in range(n):
                matrix1[i][j] = A[i][j]
        
        # invers matrix 1
        matrix1_inv = np.linalg.inv(matrix1)

        # matrix 2 (konstanta)
        for i in range(n):
            for j in range(n, n+1):
                matrix2[i] = A[i][j]

        # kalikan matrix 1 dan matrix 2
        result = np.dot(matrix1_inv, matrix2)

        end = time.time()
        calculation_time = end - start

        # tampilkan hasil
        print('\nINVERSION: ')
        label = 'a'
        for i in range(n):
            print(label.strip(), "= %0.2f;" %(result[i]), end = " ")
            label = chr(ord(label) + 1)
        print(" Calculation time: %0.5fs" %(calculation_time))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
# if __name__ == "__main__":
#     inversion = Inversion()

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

#     inversion.inversion(n, a)