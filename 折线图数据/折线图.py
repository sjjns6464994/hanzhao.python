import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
# 读取文件
f_us = open("D://python数据//资料//资料//可视化案例数据//折线图数据//美国.txt", "r", encoding = "utf-8")
f_jp = open("D://python数据//资料//资料//可视化案例数据//折线图数据//日本.txt", "r", encoding = "utf-8")
f_in = open("D://python数据//资料//资料//可视化案例数据//折线图数据//印度.txt", "r", encoding = "utf-8")
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()
# 剔除多余数据
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 将json文件转化为字典形
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# y轴数据
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图像
line = Line()
# x轴是公用的
line.add_xaxis(us_x_data)
# y轴数据
line.add_yaxis("美国确诊人数",us_y_data)
line.add_yaxis("日本确诊人数",jp_y_data)
line.add_yaxis("印度确诊人数",in_y_data)
# 设置全局选项
line.set_global_opts(
    #设置标题格式
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom = "1%")
)
# 调用render方法,生成图像
line.render()
# 关闭文件
f_us.close()
f_jp.close()
f_in.close()