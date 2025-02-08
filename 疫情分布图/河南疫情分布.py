"""
河南疫情分布图
"""

import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据
f = open("D://python数据//资料//资料//可视化案例数据//地图数据//疫情.txt", "r", encoding= "utf-8")
data = f.read()
# 关闭文件
f.close()
# 将字符串json转化为python文件
data_dict = json.loads(data)
# 取出信息
cities_data = data_dict["areaTree"][0]["children"][3]['children']

data_list = []

for city_data in cities_data:
    city_name = city_data["name"] + '市'
    city_confirm = city_data['total']["confirm"]
    data_list.append((city_name, city_confirm))
# 手动添加济源市确诊人数
data_list.append(("济源市", 5))
# print(data_list)
# 添加地图
map = Map()
map.add("河南省确诊人数", data_list, '河南')
map.set_global_opts(
    title_opts=TitleOpts(title = "全国疫情地图"),
    visualmap_opts = VisualMapOpts(
        is_show=True,       #映射是否显示
        is_piecewise=True,   #是否分段
        pieces=[
            {"min":1, "max":99, "label":"1-99", "color":"#CCFFFF"},
            {"min":100, "max":999, "label":"100-999", "color":"#FFFF99"},
            {"min":1000, "max":4999, "label":"1000-4999", "color":"#FF9966"},
            {"min":5000, "max":9999, "label":"5000-9999", "color":"#FF6666"},
        ]
    )
)

map.render("河南省疫情地图.html")