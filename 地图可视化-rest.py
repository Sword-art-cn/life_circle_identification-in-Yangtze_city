import matplotlib
matplotlib.use('TkAgg')
matplotlib.rc("font",family='YouYuan')
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import fiona

# 文件路径
input_shp_folder = r"输入\SHP文件"
output_img_folder = r"输出\可视化文件"
output_shp_folder = r"输出\SHP文件"

updated_shp_path = os.path.join(output_shp_folder, "摩擦因子某休息日跨区出行OD.shp")
base_map_path = os.path.join(input_shp_folder, "上海与扬子江城市群.shp")

with fiona.Env(encoding='GBK'):
    od_gdf = gpd.read_file(updated_shp_path)
    base_map_gdf = gpd.read_file(base_map_path)

plt.figure(figsize=(10, 10))
ax = plt.gca()
# 绘制底图
base_map_gdf.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.5, linewidth=0.5)

# 添加县区名称
for x, y, label in zip(base_map_gdf .geometry.centroid.x, base_map_gdf .geometry.centroid.y, base_map_gdf ['NAME']):
    ax.text(x, y, label, ha='center', va='center', fontsize=8, color='black')

# 绘制OD出行线路，线宽根据“count”值设置
od_gdf.plot(ax=ax, linewidth=od_gdf['count'] / od_gdf['count'].max() * 5, color='blue', alpha=0.7)

# 设置底图、标题、坐标轴和其他美化
ax.set_title("休息日跨区出行摩擦因子可视化图（线条宽度由'F'决定）", fontsize=15)
ax.set_xlabel("经度")
ax.set_ylabel("纬度")
ax.set_axis_off()

# 保存可视化结果
plt.savefig(os.path.join(output_img_folder, "restday_city_F_visualization.png"), dpi=300)
print("地图可视化已保存。")