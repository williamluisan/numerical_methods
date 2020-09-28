"""
    code credit: https://rosettacode.org/wiki/Cramer%27s_rule#Prolog
"""

import numpy as np
import sys
import time

class CramerRule:
    def cramer_rule(self, n, matrix):
        A = np.zeros((n, n))
        B = np.zeros(n)
        C = np.zeros((n, n))
        X = []
        
        start = time.time()

        # matrix 1 (A)
        for i in range(n):
            for j in range(n):
                A[i][j] = matrix[i][j]
        
        # C matriks pembagi
        for i in range(n):
            for j in range(n):
                C[i][j] = matrix[i][j]

        # matrix 2 (B) (konstanta)
        for i in range(n):
            for j in range(n, n+1):
                B[i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                C[j][i] = B[j]
                if i > 0:
                    C[j][i-1] = A[j][i-1]
            X.append(round(np.linalg.det(C) / np.linalg.det(A), 1))
        
        end = time.time()
        calculation_time = end - start
        
        # tampilkan hasil
        print("\nCRAMER'S RULE: ")
        label = 'a'
        for i in range(n):
            print(label.strip(), "= %0.2f;" %(X[i]), end = " ")
            label = chr(ord(label) + 1)
        print(" Calculation time: %0.5fs" %(calculation_time))

### UNCOMMENT THIS IF THE SCRIPT WANT TO BE EXECUTED ALONE ###
# if __name__ == "__main__":
    # cramer = CramerRule()

    # # jumlah n persamaan yang akan diselesaikan
    # n = int(input('Jumlah (n) persamaan: '))

    # a = np.zeros((n,n+1))
    # x = np.zeros(n)

    # # Memasukkan input matrix
    # print("\nMasukkan input persamaan dalam bentuk matrix (mtx) %dx%d" %(n, n))
    # for i in range(n):
    #     for j in range(n+1):
    #         a[i][j] = float(input( 'mtx['+str(i)+']['+ str(j)+']='))

    # # print matrix
    # print("\n MATRIX PERSAMAAN")
    # print(a, "\n")

    # cramer.cramer_rule(n, a)