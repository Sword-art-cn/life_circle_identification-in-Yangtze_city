import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 读取数据
od_data_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\CSV文件\某工作日跨区出行OD.csv"
area_base_path = "workday_area_base.csv"

od_data = pd.read_csv(od_data_path, encoding="GBK")
area_base = pd.read_csv(area_base_path, encoding="GBK")

# 将区数据转换为字典，方便查找出行发生量（O）和吸引量（D）
o_dict = area_base.set_index('AREA')['O'].to_dict()
d_dict = area_base.set_index('AREA')['D'].to_dict()

# 2. 假设初始模型系数 K0=1，计算 F0
od_data['P'] = od_data['OAREA'].map(o_dict)  # 出行发生量
od_data['A'] = od_data['DAREA'].map(d_dict)  # 吸引量

# 计算 F0：假设 T = count，K = 1
od_data['F0'] = od_data['count'] / (od_data['P'] * od_data['A'])
f0_result = od_data[['OAREA', 'DAREA', 'F0']]

# 3. 计算 ADDF0 和更新 K
add_f0 = f0_result['F0'].sum()
K = 1 / add_f0

# 4. 使用更新后的 K 重新计算 F
od_data['F'] = od_data['count'] / (K * od_data['P'] * od_data['A'])
f_result = od_data[['OAREA', 'DAREA', 'F']]

# 5. 输出 F0 结果为 "workday_city_F0.csv"
f0_result.to_csv("workday_city_F0.csv", index=False, encoding="GBK")

# 输出 F 结果为 "workday_city_F.csv"
f_result.to_csv("workday_city_F.csv", index=False, encoding="GBK")

# 6. 优化结构：将结果重塑为矩阵形式，横轴为 OAREA，纵轴为 DAREA，值为 F
pivot_result = f_result.pivot(index='DAREA', columns='OAREA', values='F')
pivot_result.to_csv("workday_city_F_reshape.csv", encoding="GBK")

print("计算完成，结果已保存。")
