import pandas as pd
import numpy as np

# 1. 读取数据
data = pd.read_csv(r'C:\Users\haolipu\Desktop\daily learning\Python学习\Python打卡第五天\data.csv')

# 2. 找到所有离散变量
discrete_features = []
for column in data.columns:
    if data[column].dtype == 'object':
        discrete_features.append(column)

print("离散变量列表：", discrete_features)

# 3. 对离散变量进行独热编码
data = pd.get_dummies(data, columns=discrete_features, drop_first=True)

# 4. 找出独热编码后新增的列
original_data = pd.read_csv(r'C:\Users\haolipu\Desktop\daily learning\Python学习\Python打卡第五天\data.csv')
original_columns = original_data.columns
new_columns = [col for col in data.columns if col not in original_columns]

print("\n独热编码后新增的列：", new_columns)

# 5. 将独热编码的结果转换为int类型
data[new_columns] = data[new_columns].astype(int)

# 6. 处理所有列的缺失值
numeric_columns = data.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    missing_count = data[column].isnull().sum()
    if missing_count > 0:
        print(f"\n列 '{column}' 有 {missing_count} 个缺失值")
        # 使用更安全的方式填充缺失值
        data.loc[:, column] = data[column].fillna(data[column].mean())

# 7. 验证是否还有缺失值
remaining_nulls = data.isnull().sum().sum()
print(f"\n处理后剩余的缺失值总数：{remaining_nulls}")

# 8. 保存处理后的数据
data.to_csv(r'C:\Users\haolipu\Desktop\daily learning\Python学习\Python打卡第五天\processed_data.csv', index=False)

print("\n数据处理完成！")
print(f"处理后的数据维度：{data.shape}")