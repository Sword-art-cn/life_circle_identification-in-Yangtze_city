import geopandas as gpd
import pandas as pd
import fiona

# 1. 读取原始SHP文件和dbf_df数据
shp_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\某工作日跨区出行OD\某工作日跨区出行OD.shp"
with fiona.Env(encoding='GBK'):
    od_gdf = gpd.read_file(shp_path)

# 读取dbf_df数据，其中包含了更新的count列
dbf_df_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\输出\某工作日跨区出行OD\摩擦因子某工作日跨区出行OD.csv"
dbf_df = pd.read_csv(dbf_df_path, encoding='gbk')

# 2. 将dbf_df中的数据与od_gdf进行合并，基于【OAREA】和【DAREA】进行匹配
od_gdf = od_gdf.merge(dbf_df[['OAREA', 'DAREA', 'count']], on=['OAREA', 'DAREA'], how='left', suffixes=('', '_new'))

# 3. 使用dbf_df的count值替换原来的count值（如果dbf_df中有对应的count数据）
od_gdf['count'] = od_gdf['count_new'].fillna(od_gdf['count'])
od_gdf = od_gdf.drop(columns=['count_new'])  # 删除临时列

# 4. 将更新后的GeoDataFrame导出为新的SHP文件
updated_shp_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\输出\某工作日跨区出行OD\摩擦因子某工作日跨区出行OD.shp"
with fiona.Env(encoding='GBK'):
    od_gdf.to_file(updated_shp_path, encoding="GBK")

print("SHP文件更新完成并已保存为新的文件。")


