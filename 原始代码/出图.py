import matplotlib
matplotlib.use('TkAgg')
matplotlib.rc("font",family='YouYuan')

import geopandas as gpd
import matplotlib.pyplot as plt
import fiona  # 确保Fiona使用正确的编码
import contextily as ctx

# 1. 导入并读取已更新的Shp文件
updated_shp_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\输出\某工作日跨区出行OD\摩擦因子某工作日跨区出行OD.shp"
base_map_path = r"C:\Users\DELL\Desktop\作业文件\国土空间与城市规划\作业二：区域联系分析\扬子江\SHP文件\上海与扬子江城市群\上海与扬子江城市群.shp"

# 确保使用GBK编码以正确读取中文字符
with fiona.Env(encoding='GBK'):
    od_gdf = gpd.read_file(updated_shp_path)
    base_map_gdf = gpd.read_file(base_map_path)

# 2. 绘制地图，设置线宽与“count”值成比例
plt.figure(figsize=(10, 10))
ax = plt.gca()

# 绘制底图
base_map_gdf.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.5, linewidth=0.5)

# 添加县区名称
for x, y, label in zip(base_map_gdf .geometry.centroid.x, base_map_gdf .geometry.centroid.y, base_map_gdf ['NAME']):
    ax.text(x, y, label, ha='center', va='center', fontsize=1, color='black')

# 绘制OD出行线路，线宽根据“count”值设置
od_gdf.plot(
    ax=ax,
    linewidth=od_gdf['count'] / od_gdf['count'].max() * 5,  # 调整线宽比例
    color='blue',
    alpha=0.7
)

# 3. 设置底图、标题、坐标轴和其他美化
ax.set_title("工作日跨区出行摩擦因子可视化图（线条宽度由'F'决定）", fontsize=15)
ax.set_xlabel("经度")
ax.set_ylabel("纬度")
ax.set_axis_off()

plt.grid(True)
plt.show()
