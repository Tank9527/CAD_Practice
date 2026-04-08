"""
Day 2 - Part 1 补充: 列表进阶训练
场景：更贴近 CAD 工程师实际工作中的列表处理
"""

# ============================================================
# 练习 5: 仿真 Spec 检查报告
# ============================================================
# 根据 spec 要求，逐项检查每个 corner 的仿真结果是否 pass
# 并生成一份汇总报告

results = [
    ("tt_25c",  45.67, 62.3, 125.8),
    ("ss_125c", 38.21, 55.1,  89.3),
    ("ff_m40c", 52.04, 70.8, 198.2),
    ("ss_m40c", 36.88, 51.2,  75.6),
    ("ff_125c", 41.05, 58.9, 145.0),
]
# 格式: (corner, gain_dB, pm_deg, gbw_MHz)

# Spec 要求:
#   Gain >= 40 dB
#   PM   >= 55 deg
#   GBW  >= 80 MHz

# 对每个 corner 打印 PASS/FAIL:
#   tt_25c   : Gain=45.67 PASS | PM=62.3 PASS | GBW=125.8 PASS -> ALL PASS
#   ss_m40c  : Gain=36.88 FAIL | PM=51.2 FAIL | GBW=75.6  FAIL -> FAIL
# 最后统计: "X/5 corners 全部通过"

# >>> 在这里写代码 <<<
pass_count = 0
for corner, gain, pm,  gbw in results:
    if gain >= 40 and pm >= 55 and gbw >= 80:
        print(f"{corner:10} : Gain={gain:6.2f} PASS | PM={pm:6.1f} PASS |GBW={gbw:6.1f} PASS -> ALL PASS")
        pass_count += 1
    else:
        print(f"{corner:10} : Gain={gain:6.2f} {'PASS' if gain >= 40 else 'FAIL'} | PM={pm:6.1f} {'PASS' if pm >= 55 else 'FAIL'} |GBW={gbw:6.1f} {'PASS' if gbw >= 80 else 'FAIL'} -> FAIL")  
print(f"{pass_count}/{len(results)} corners 全部通过")      

# ============================================================
# 练习 6: Wafer Map 数据处理
# ============================================================
# 一个简化的 wafer map，每个 die 有一个良率测试结果
# 1 = pass, 0 = fail, -1 = 未测试

wafer_map = [
    [-1,  1,  1,  1, -1],
    [ 1,  1,  0,  1,  1],
    [ 1,  0,  1,  1,  1],
    [ 1,  1,  1,  0,  1],
    [-1,  1,  1,  1, -1],
]

# (a) 统计 pass、fail、未测试 的 die 数量
# (b) 计算良率 = pass / (pass + fail) * 100%（不算未测试的）
# (c) 找出所有 fail 的坐标，格式 [(row, col), ...]
#     期望: [(1,2), (2,1), (3,3)]
# 提示: 用 enumerate 遍历二维列表拿到行列索引

# >>> 在这里写代码 <<<
pass_count = 0
fail_count = 0
untested_count = 0
fail_index_list = []
for index_row, row in enumerate(wafer_map):
    for index_col, die in enumerate(row):
        if die == 1:
            pass_count += 1
        elif die == 0:
            fail_count += 1
            fail_index_list.append((index_row,index_col)) #把fail的坐标加入列表
        elif die == -1:
            untested_count += 1
print(f'PASS数量: {pass_count}, FAIL数量: {fail_count}, 未测试数量: {untested_count}')
print(f'良率： {pass_count / (pass_count + fail_count):.2%}')
print(f'fail坐标列表: {fail_index_list}')

# ============================================================
# 练习 7: Corner 列表分组
# ============================================================
# 把 corner 列表按 process 类型分组

all_corners = [
    "ss_1.62V_m40C", "ss_1.62V_25C", "ss_1.62V_125C",
    "tt_1.8V_m40C",  "tt_1.8V_25C",  "tt_1.8V_125C",
    "ff_1.98V_m40C", "ff_1.98V_25C", "ff_1.98V_125C",
    "ss_1.8V_25C",   "ff_1.8V_25C",
]

# 按 process (ss/tt/ff) 分组，结果存成字典:
# {
#   "ss": ["ss_1.62V_m40C", "ss_1.62V_25C", "ss_1.62V_125C", "ss_1.8V_25C"],
#   "tt": ["tt_1.8V_m40C", "tt_1.8V_25C", "tt_1.8V_125C"],
#   "ff": ["ff_1.98V_m40C", "ff_1.98V_25C", "ff_1.98V_125C", "ff_1.8V_25C"],
# }
# 提示: corner 名的第一个 "_" 前面就是 process
# 打印每组的名称和数量

# >>> 在这里写代码 <<<
process_dict = {}
for corner in all_corners:
    #if corner.startswith("ss" or "tt" or "ff"): #如果corner以ss、tt或ff开头
    process = corner.split("_")[0]
    if process not in process_dict:
        process_dict[process] = [corner] #如果process不在字典里，创建一个新的键值对，值是一个包含当前corner的列表
    else:
        process_dict[process].append(corner) #如果process已经在字典里了，就把当前corner添加到对应的列表里
for process, corners in process_dict.items():
    print(f"Process: {process}, Corners: {corners}, Count: {len(corners)}")


# ============================================================
# 练习 8: 仿真结果排序与筛选
# ============================================================
# 多个 cell 的仿真结果，按不同指标排序

cell_results = [
    ("LDO_TOP",  45.67, 62.3, 125.8, 2.35),
    ("BANDGAP",  38.21, 75.1,  89.3, 0.85),
    ("VCO_CORE", 52.04, 50.8, 198.2, 5.10),
    ("OTA_V3",   48.90, 68.5, 155.0, 1.20),
    ("COMP_V1",  30.55, 80.2,  65.0, 0.45),
    ("BIAS_GEN", 25.00, 90.0,  40.0, 0.15),
]
# 格式: (cell, gain_dB, pm_deg, gbw_MHz, power_mW)

# (a) 按 gain 从高到低排序，打印排名
#     提示: sorted(list, key=lambda x: x[1], reverse=True)
#     lambda 就是一个临时的小函数，x 代表列表里的每个元素（一个 tuple）
#     x[1] 表示按 tuple 的第2个值（gain）来排序

# (b) 按 power 从低到高排序，打印排名

# (c) 找出 "性价比最高" 的 cell: gbw / power 最大的
#     打印 cell 名和对应的 gbw/power 值

# >>> 在这里写代码 <<<
sorted_by_gain = sorted(cell_results, key=lambda x: x[1], reverse=True) #按gain从高到低排序，x[1]表示按tuple的第2个值（gain）来排序
print(f"按gain降序排列: {sorted_by_gain}")
sorted_by_power = sorted(cell_results,key=lambda x: x[4]) #按power从低到高排序，x[4]表示按tuple的第5个值（power）来排序
print(f"按power升序排列: {sorted_by_power}")
max_gbw_power_ratio_cell = max(cell_results, key=lambda x: x[3]/x[4]) #找出gbw/power最大的cell，x[3]表示gbw，x[4]表示power
print(f"性价比最高的cell: {max_gbw_power_ratio_cell[0]}, gbw/power = {max_gbw_power_ratio_cell[3]/max_gbw_power_ratio_cell[4]:.2f}")    


# ============================================================
# 练习 9: 列表模拟 Monte Carlo 统计
# ============================================================
# 模拟 Monte Carlo 仿真结果分析

import random
random.seed(42)  # 固定随机种子，保证每次运行结果一样

# 生成 100 次仿真的 gain 值（正态分布，均值 45dB，标准差 3dB）
mc_gains = [round(random.gauss(45, 3), 2) for _ in range(100)]

# (a) 打印前 10 个值
# (b) 计算均值 mean = sum(list) / len(list)
# (c) 计算最大值、最小值、range = max - min
# (d) 统计落在 [42, 48] 范围内的比例（即 ±1sigma 范围）
# (e) 按值排序后，找出第 5 和第 95 百分位的值
#     第5百分位 = 排序后第 5 个（索引4）
#     第95百分位 = 排序后第 95 个（索引94）
#     打印: "5th percentile: XX.XX dB, 95th percentile: XX.XX dB"

# >>> 在这里写代码 <<<
print(f"前10个gain值:{mc_gains[:10]}") #打印前10个值，切片[:10]表示从索引0到索引9的元素
mean_gain = sum(mc_gains) / len(mc_gains) #计算均值，sum()函数计算列表元素的总和，len()函数计算列表的长度
print(f"均值: {mean_gain:.2f} dB") #打印均值，保留两位小数
max_gain = max(mc_gains) #计算最大值，max函数返回列表中的最大值
min_gain = min(mc_gains) #计算最小值，min函数返回列表中的最小值
gain_range = max_gain - min_gain #计算范围  
print(f"最大值: {max_gain:.2f} dB, 最小值: {min_gain:.2f} dB, 范围: {gain_range:.2f} dB") #打印最大值、最小值和范围，保留两位小数
#count_in_range = sum(x for x in mc_gains if 42<= x <= 48) #统计落在[42,48]范围内的值的数量，生成器表达式x for x in mc_gains if 42<=x<=48会遍历mc_gains列表，满足条件的x会被sum()函数累加
count_in_range = sum(1 for x in mc_gains if 42<= x <= 48) #统计落在[42,48]范围内的值的数量，生成器表达式x for x in mc_gains if 42<=x<=48会遍历mc_gains列表，满足条件的x会被sum()函数累加
proportion_in_range = count_in_range / len(mc_gains) #计算比例，count_in_range是满足条件的数量，len(mc_gains)是总数量
print(f"落在[42,48]范围内的比例: {proportion_in_range:.2%}") #打印比例，保留两位小数
sorted_gains = sorted(mc_gains) #按值排序，sorted()函数返回一个新的排序后的列表
fifth_percentile = sorted_gains[4] #第5百分位的值，索引4表示排序后列表中的第5个元素
ninety_fifth_percentile = sorted_gains[94] #第95百分位的值，索引94表示排序后列表中的第95个元素
print(f"5th percentile: {fifth_percentile:.2f} dB, 95th percentile: {ninety_fifth_percentile:.2f} dB") #打印第5和第95百分位的值，保留两位小数l

