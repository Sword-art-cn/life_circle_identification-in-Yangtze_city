import geopandas as gpd
import os
import pandas as pd

# 文件路径
input_shp_folder = r"输入\SHP文件"
output_shp_folder = r"输出\SHP文件"
input_folder = r"输入\CSV文件"
output_folder = r"输出\CSV文件"

shp_path = os.path.join(input_shp_folder, "某休息日跨区出行OD.shp")
f_df_path = os.path.join(output_folder, "restday_city_F.csv")
od_gdf = gpd.read_file(shp_path)
f_df = pd.read_csv(f_df_path, encoding='GBK')

# 筛选前10%的 F 数据并更新 SHP 文件
threshold = int(len(f_df) * 0.1)
f_df.loc[threshold:, 'F'] = 0
f_df.to_csv(os.path.join(output_folder, "restday_city_F_pro.csv"), index=False, encoding='gbk')

# 合并并输出新 SHP 文件
file_path = os.path.join(input_folder, "某休息日跨区出行OD.csv")
dbf_df = pd.read_csv(file_path, encoding="GBK")
dbf_df = dbf_df.merge(f_df[['OAREA', 'DAREA', 'F']], on=['OAREA', 'DAREA'], how='left')
dbf_df['count'] = dbf_df['F'].fillna(0) * (10 ** 10)
updated_shp_path = os.path.join(output_shp_folder, "摩擦因子某休息日跨区出行OD.shp")
od_gdf.to_file(updated_shp_path, encoding="GBK")
print("SHP 文件已保存。")