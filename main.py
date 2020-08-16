from pygraphblas import *
from tqdm import tqdm
from cfpq_data_devtools.filters import get_file_len

A = Matrix.sparse(BOOL, 5, 5)
B = Matrix.sparse(BOOL, 5, 5)
A[1, 2] = True
B[2, 3] = True

print(list(A), list(B))
assert list(A @ B) == [(1, 3, True)]

for i in tqdm(range(100), desc="Testing tqdm"):
    pass

print(get_file_len(__file__))
