import numpy as np
from scipy import stats

# 設定數據集
data = [10, 12, 15, 14, 13, 12, 13, 12, 14]

# 計算平均值
mean = np.mean(data)  # 使用 NumPy 函式計算數據的平均值

# 計算中位數
median = np.median(data)  # 使用 NumPy 函式計算數據的中位數

# 計算眾數
mode = stats.mode(data).mode[0]  # 使用 SciPy 函式計算數據的眾數

# 計算標準差
std_dev = np.std(data)  # 使用 NumPy 函式計算數據的標準差

# 輸出結果
print(f"平均值: {mean}")
print(f"中位數: {median}")
print(f"眾數: {mode}")
print(f"標準差: {std_dev}")