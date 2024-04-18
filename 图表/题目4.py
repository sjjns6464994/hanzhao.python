import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rc("font", family='Microsoft YaHei')

# 创建DataFrame
zcfz = pd.DataFrame({
    '资产合计': [319598183780.38, 279217923628.27, 282972157415.28,  251234157276.81, 214967999328.38],
    '负债合计': [211672732613.87, 162337436540.13, 170924500892.20, 158519445549.35, 148133201565.19],
    '所有者权益': None
})
zcfz.index = [2021, 2020, 2019, 2018, 2017]

# 计算所有者权益
zcfz['所有者权益'] = zcfz['资产合计'] - zcfz['负债合计']

# 计算资产负债率
zcfz['资产负债率'] = zcfz['负债合计'] / zcfz['资产合计']

# 计算产权比率
zcfz['产权比率'] = zcfz['所有者权益'] / zcfz['资产合计']

# 计算权益乘数
zcfz['权益乘数'] = zcfz['资产合计'] / zcfz['所有者权益']

# 绘制资产负债率、产权比率和权益乘数的折线图
plt.plot(zcfz.index, zcfz['资产负债率'], label='资产负债率', linestyle='--')
plt.plot(zcfz.index, zcfz['产权比率'], label='产权比率')
plt.plot(zcfz.index, zcfz['权益乘数'], label='权益乘数')
plt.legend()

# 添加标签和标题
plt.xlabel('时间')
plt.ylabel('比率')
plt.title('企业财务比率分析')

# 显示图表
plt.show()
