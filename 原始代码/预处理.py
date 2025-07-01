import pandas as pd

# 1. 导入CSV文件为DataFrame
file_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\CSV文件\某工作日跨区出行OD.csv"
df = pd.read_csv(file_path, encoding="GBK")

# 2. 计算所有区的出行发生量“O”和吸引量“D”
area_o = df.groupby('OAREA')['count'].sum().reset_index().rename(columns={'count': 'O'})
area_d = df.groupby('DAREA')['count'].sum().reset_index().rename(columns={'count': 'D'})
area_base = pd.merge(area_o, area_d, left_on='OAREA', right_on='DAREA', how='outer').fillna(0)
area_base = area_base.rename(columns={'OAREA': 'AREA'})[['AREA', 'O', 'D']]

# 3. 记录结果
# 保存为表格“workday_area_base.csv”
area_base.to_csv("workday_area_base.csv", index=False, encoding="GBK")

# 4. 计算所有市的出行发生量“O”和吸引量“D”
city_o = df.groupby('OCITY')['count'].sum().reset_index().rename(columns={'count': 'O'})
city_d = df.groupby('DCITY')['count'].sum().reset_index().rename(columns={'count': 'D'})
city_base = pd.merge(city_o, city_d, left_on='OCITY', right_on='DCITY', how='outer').fillna(0)
city_base = city_base.rename(columns={'OCITY': 'CITY'})[['CITY', 'O', 'D']]

# 保存为“workday_city_base.csv”
city_base.to_csv("workday_city_base.csv", index=False, encoding="GBK")

# 5. 计算所有省的出行发生量“O”和吸引量“D”
prov_o = df.groupby('OPROV')['count'].sum().reset_index().rename(columns={'count': 'O'})
prov_d = df.groupby('DPROV')['count'].sum().reset_index().rename(columns={'count': 'D'})
prov_base = pd.merge(prov_o, prov_d, left_on='OPROV', right_on='DPROV', how='outer').fillna(0)
prov_base = prov_base.rename(columns={'OPROV': 'PROV'})[['PROV', 'O', 'D']]

# 保存为“workday_prov_base.csv”
prov_base.to_csv("workday_prov_base.csv", index=False, encoding="GBK")

print("数据处理完成并保存。")
