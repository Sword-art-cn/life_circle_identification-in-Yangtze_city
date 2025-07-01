import pandas as pd
import os

# 设置路径
input_folder = r"输入\CSV文件"
output_folder = r"输出\CSV文件"

# 导入数据
od_data_path = os.path.join(input_folder, "某休息日跨区出行OD.csv")
area_base_path = os.path.join(output_folder, "restday_area_base.csv")

od_data = pd.read_csv(od_data_path, encoding="GBK")
area_base = pd.read_csv(area_base_path, encoding="GBK")

# 假设初始系数 K0 = 1，计算 F0
od_data['P'] = od_data['OAREA'].map(area_base.set_index('AREA')['O'])
od_data['A'] = od_data['DAREA'].map(area_base.set_index('AREA')['D'])
od_data['F0'] = od_data['count'] / (od_data['P'] * od_data['A'])
f0_result = od_data[['OAREA', 'DAREA', 'F0']]

# 更新 K 并重新计算 F
add_f0 = f0_result['F0'].sum()
K = 1 / add_f0
od_data['F'] = od_data['count'] / (K * od_data['P'] * od_data['A'])

# 保存计算结果
f0_result.to_csv(os.path.join(output_folder, "restday_city_F0.csv"), index=False, encoding="GBK")
od_data[['OAREA', 'DAREA', 'F']].to_csv(os.path.join(output_folder, "restday_city_F.csv"), index=False, encoding="GBK")

# 优化结构：将结果重塑为矩阵形式，横轴为 OAREA，纵轴为 DAREA，值为 F
pivot_result = od_data.pivot(index='DAREA', columns='OAREA', values='F')
pivot_result.to_csv(os.path.join(output_folder, "restday_city_F_reshape.csv"), encoding="GBK")

print("模型计算完成并保存。")