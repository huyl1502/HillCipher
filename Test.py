import numpy as np

K = np.array([[1,2,3],[3,5,5],[4,5,6]])
dK = np.linalg.det(K)
iK = (np.linalg.inv(K))
rs = dK * iK
rs = np.around(rs)
rs = rs.astype(int)
print(rs)