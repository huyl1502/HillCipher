import numpy as np
MOD = 37
K = np.array([[1,2],[3,4]])
dK = int(np.linalg.det(K))
idK = pow(dK,-1,MOD)
print(idK)
Pk = dK*np.linalg.inv(K)
for i in range(len(Pk)):
    for j in range(len(Pk[i])):
        if Pk[i][j] < 0:
            Pk[i][j] += MOD
        Pk[i][j] = int((Pk[i][j] * idK) % MOD)
print(Pk)        
