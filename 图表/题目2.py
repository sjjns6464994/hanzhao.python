original_value = 90000  # 固定资产原值
depreciation_years = 10  # 折旧年限
salvage_rate = 0.05  # 固定资产残值率

annual_depreciation = (1 - salvage_rate) * original_value / depreciation_years  # 每年的折旧额
accumulated_depreciation = 0  # 累计折旧额
depreciation_list = []  # 折旧额列表

for i in range(1, depreciation_years + 1):
    accumulated_depreciation += annual_depreciation

    # 将每年的折旧额添加到列表中
    depreciation_list.append(round(annual_depreciation, 2))

print(depreciation_list)  # 输出折旧额列表

