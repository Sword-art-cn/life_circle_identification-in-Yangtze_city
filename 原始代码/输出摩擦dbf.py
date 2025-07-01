import pandas as pd
import geopandas as gpd

# 9. 导入SHP文件数据（仅展示其中的主要代码逻辑）
shp_path = r"C:\\Users\\DELL\\Desktop\\作业文件\\国土空间与城市规划\\作业二：区域联系分析\\扬子江\\SHP文件\\某工作日跨区出行OD\\某工作日跨区出行OD.shp"
od_gdf = gpd.read_file(shp_path)

# 10. 筛选前10% F 的数据
f_df = pd.read_csv("workday_city_F.csv", encoding='gbk')
f_df = f_df.sort_values(by='F', ascending=False)
threshold = int(len(f_df) * 0.1)
f_df.loc[threshold:, 'F'] = 0  # 保留前10%数据，其余设为0
f_df.to_csv("workday_city_F_pro.csv", index=False, encoding='gbk')

# 10.2 将 F 数据优化为矩阵格式
f_pro_matrix = f_df.pivot(index='DAREA', columns='OAREA', values='F').fillna(0)
f_pro_matrix.to_csv("workday_city_F_pro_reshape.csv", encoding='gbk')

from simpledbf import Dbf5
# 11. 合并 dbf 数据
dbf_df = pd.read_excel(r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\某工作日跨区出行OD\某工作日跨区出行OD.xlsx")
dbf_df = dbf_df.merge(f_df[['OAREA', 'DAREA', 'F']], on=['OAREA', 'DAREA'], how='left')
dbf_df['F'] = dbf_df['F'].fillna(0) * (10 ** 10)  # 缺失值设为0，并放大
# 修改 count 列的值为F列的值
dbf_df['count'] = dbf_df['F']
# 删除 F 列
dbf_df.drop(columns=['F'], inplace=True)
dbf_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\输出\某工作日跨区出行OD\摩擦因子某工作日跨区出行OD.csv"
dbf_df.to_csv(dbf_path.replace('.dbf', '.csv'), index=False, encoding='gbk')



