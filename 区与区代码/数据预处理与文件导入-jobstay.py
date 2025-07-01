import pandas as pd
import os

# 文件路径设置
input_folder = r"输入\CSV文件"
output_folder = r"输出\CSV文件"

# 导入 CSV 文件
file_path = os.path.join(input_folder, "区与区之间的职住OD.csv")
df = pd.read_csv(file_path, encoding="GBK")

# 计算区的出行发生量 "O" 和吸引量 "D"
area_o = df.groupby('OAREA')['count'].sum().reset_index().rename(columns={'count': 'O'})
area_d = df.groupby('DAREA')['count'].sum().reset_index().rename(columns={'count': 'D'})
area_base = pd.merge(area_o, area_d, left_on='OAREA', right_on='DAREA', how='outer').fillna(0)
area_base = area_base.rename(columns={'OAREA': 'AREA'})[['AREA', 'O', 'D']]

# 输出区级数据
area_base.to_csv(os.path.join(output_folder, "jobstay_area_base.csv"), index=False, encoding="GBK")
print("区级数据保存完成。")