"""
演示疫情可视化地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取文件
f = open("D://python数据//资料//资料//可视化案例数据//地图数据//疫情.txt", "r", encoding= "utf-8")
data = f.read()  #得到全部文件
# 关闭文件
f.close()
# 将字符串json转化为python的字典
data_dict = json.loads(data)
# 从字典中取出省份的信息
province_data_list = data_dict["areaTree"][0]["children"]
# print(province_data_list)
# 直辖市
municipalities = ["北京", "天津", "上海", "重庆"]
# 自治区
special_1= ["内蒙古","西藏"]
special_2= ["新疆"]
special_3= ["广西"]
special_4= ["宁夏"]
# 澳门，香港
special_5= ["澳门", "香港"]
# 组装每个省份和确诊人数为元组，并将各个省份的数据都装入列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]      #省份名称
    if "省" not in province_name:
        if province_name in municipalities:
            province_name = province_name + "市"
        elif province_name in special_1:
            province_name = province_name + "自治区"
        elif province_name in special_2:
            province_name = province_name + "维吾尔自治区"
        elif province_name in special_3:
            province_name = province_name + "壮族自治区"
        elif province_name in special_4:
            province_name = province_name + "回族自治区"
        elif province_name in special_5:
            province_name = province_name + "特别行政区"
        else:
            province_name = province_name + "省"
    province_confirm = province_data["total"]["confirm"] #确诊人数
    data_list.append((province_name, province_confirm))
print(data_list)
# 创建地图
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局选项
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
            {"min":10000, "max":99999, "label":"10000-99999", "color":"#CC3333"},
            {"min":100000, "label":"100000+", "color":"#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情分布.html")





