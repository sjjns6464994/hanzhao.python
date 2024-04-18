import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rc("font", family='Microsoft YaHei')
# 读取利润表
lrb = pd.read_excel('利润表.xlsx')

# 生成营业收入柱状图
plt.bar(lrb['报表项目'], lrb['营业收入'], color='red', edgecolor='black')
plt.xlabel('报表项目')
plt.ylabel('营业收入')
plt.title('营业收入柱状图')
plt.show()

# 计算营业毛利和毛利率
lrb['营业毛利'] = lrb['营业收入'] - lrb['营业成本']
lrb['毛利率'] = lrb['利润总额'] / lrb['营业收入']

# 绘制毛利率折线图
plt.plot(lrb['报表项目'], lrb['毛利率'], 'o--', color='red')
plt.xlabel('报表项目')
plt.ylabel('毛利率')
plt.title('毛利率折线图')
plt.show()

# 绘制各年净利润饼图
net_profit = lrb.groupby('报表项目')['净利润'].sum()
plt.pie(net_profit, labels=net_profit.index, autopct='%1.1f%%')
plt.title('净利润饼图')
plt.show()

