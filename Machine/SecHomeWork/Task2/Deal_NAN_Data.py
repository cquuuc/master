import numpy as np
import pandas as pd


ln1 = pd.Series([1, 2], dtype=np.int64).reindex([0, 1, 2])
ln2 = pd.Series([True, False], dtype=np.bool_).reindex([0, 1, 2])
print(ln1)


ser1 = pd.isna(ln1)
print(ser1)
ser2 = pd.notna(ln1)
print(ser2)
