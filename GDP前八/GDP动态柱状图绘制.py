"""
GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
from 学习.基础时间线柱状图绘制 import timeline

# 读取数据
f = open("D://python数据//资料//资料//可视化案例数据//动态柱状图数据//1960-2019全球GDP数据.csv", "r", encoding = "GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
#删除第一条数据
data_lines.pop(0)
# 将数据转化为字典存储
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2]) #将科学计数法转换为数字
    # 如何判断字典里是否有指定的key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 每一年的数据都构建一个柱状图
# 排序年份
sorted_year_list = sorted(data_dict.keys())#keys()方法取出全部的key
# print(sorted_year_list)
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)  #升序
    #本年份前八的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/ 100000000)
#     构建柱状图数据
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
#     反转x,y轴
    bar.reversal_axis()
    # 设置没一年的的图标标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,#间隔
    is_timeline_show=True,#显示时间线
    is_auto_play=True,#是否自动播放
    is_loop_play=False,#是否循环播放
)
# 绘图
timeline.render("GDP前八的国家.html")










