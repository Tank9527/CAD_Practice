"""
Day 2 - Part 2 补充: 字典进阶训练
场景：CAD flow 脚本里的字典实战
"""

# ============================================================
# 练习 5: 工艺角参数表 (PVT 查找表)
# ============================================================
# 用嵌套字典维护不同 corner 下的器件参数

pvt_table = {
    "ss_m40c": {"vth": 0.52, "u0": 280, "vsat": 1.05e5},
    "tt_25c":  {"vth": 0.45, "u0": 320, "vsat": 1.20e5},
    "ff_125c": {"vth": 0.38, "u0": 350, "vsat": 1.35e5},
}

# (a) 打印 tt_25c 的 vth 值
# (b) 找出哪个 corner 的 vth 最大（用 max + lambda 或 max + key=...）
# (c) 算出三个 corner 的 vth 平均值
# (d) 给每个 corner 添加一个新字段 "tox": 1.85e-9
# (e) 打印一份对齐的表格:
#     Corner   |  vth  |   u0  |   vsat   |  tox
#     ---------+-------+-------+----------+--------
#     ss_m40c  | 0.52  |  280  | 1.05e+05 | 1.85e-09
#     ...

# >>> 在这里写代码 <<<
for value in pvt_table["tt_25c"].values():
    if value.key() == "vth":
        print(f"tt_25c的vth值: {value["vth"]}") #打印tt_25c的vth值

for corner, params in pvt_table.items():
    if params["vth"] == max(pvt_table.values(), key=lambda x: x["vth"])["vth"]:
        print(f"vth最大的corner: {corner}, vth = {params['vth']}") #找出哪个corner的vth最大，并打印corner名和对应的vth值

average_vth = sum(params["vth"] for params in pvt_table.values()) / len(pvt_table) #算出三个corner的vth平均值，sum函数计算所有corner的vth总和，len函数计算corner的数量
print(f"平均vth值: {average_vth:.2f}V") #打印平均vth值，保留两位小数



# ============================================================
# 练习 6: 按 owner 分组 cell（dict of list）
# ============================================================
# 把 cell 列表按 owner 分组，结果是 {owner: [cell1, cell2, ...]}

cells_info = [
    ("LDO_TOP",  "josn"),
    ("BANDGAP",  "mike"),
    ("VCO_CORE", "josn"),
    ("OTA_V3",   "alice"),
    ("COMP_V1",  "mike"),
    ("BIAS_GEN", "josn"),
    ("DAC_8B",   "alice"),
    ("ADC_12B",  "mike"),
]

# 期望:
# {
#   "josn":  ["LDO_TOP", "VCO_CORE", "BIAS_GEN"],
#   "mike":  ["BANDGAP", "COMP_V1", "ADC_12B"],
#   "alice": ["OTA_V3", "DAC_8B"],
# }
# 提示: 如果 owner 不在 dict 里，先创建空列表，再 append
# 进阶提示: dict.setdefault(key, []) 可以一行搞定

# 然后打印每个人负责的 cell 数量和列表

# >>> 在这里写代码 <<<


# ============================================================
# 练习 7: 统计 corner 出现次数（手写 Counter）
# ============================================================
# 多次仿真后，每次跑了哪些 corner 都被记录下来
# 统计每个 corner 总共跑了多少次

run_log = [
    "tt_25c", "ss_125c", "tt_25c", "ff_m40c", "ss_125c",
    "tt_25c", "ss_m40c", "ff_125c", "tt_25c", "ff_m40c",
    "ss_125c", "tt_25c", "ff_125c", "tt_25c", "ss_125c",
]

# (a) 用字典统计每个 corner 出现的次数
#     期望: {"tt_25c": 5, "ss_125c": 4, "ff_m40c": 2, "ss_m40c": 1, "ff_125c": 2}
# (b) 找出跑得最多的 corner
# (c) 找出只跑了 1 次的 corner（可能漏跑，需要补）
# (d) 按出现次数降序打印: "tt_25c: 5 次"
#     提示: sorted(dict.items(), key=lambda x: x[1], reverse=True)

# >>> 在这里写代码 <<<


# ============================================================
# 练习 8: 合并多个仿真结果字典
# ============================================================
# 不同人各自跑了一些 corner，把所有结果合并成一个总表
# 如果同一个 corner 在多个字典里出现，取**最后**那次的值（覆盖）

josn_results = {
    "tt_25c":  45.67,
    "ss_125c": 38.21,
    "ff_m40c": 52.04,
}

mike_results = {
    "ss_m40c": 36.88,
    "ff_125c": 41.05,
    "tt_25c":  45.80,    # 注意: tt_25c 在 josn 那里也有
}

alice_results = {
    "tt_m40c": 43.20,
    "ss_125c": 38.50,    # 注意: ss_125c 在 josn 那里也有
}

# (a) 合并三个字典到 all_results（mike 和 alice 的值会覆盖 josn 的）
#     提示有两种写法:
#       方法1: all_results = {}; all_results.update(josn_results); ...
#       方法2: all_results = {**josn_results, **mike_results, **alice_results}
# (b) 打印总条目数
# (c) 找出 gain 不达标 (<40) 的 corner 列表
# (d) 按 gain 升序打印所有结果

# >>> 在这里写代码 <<<


# ============================================================
# 练习 9: 反向索引（值 -> key 列表）
# ============================================================
# 每个 cell 用了哪个 process node，构建反向索引：node -> [cell1, cell2, ...]

cell_node = {
    "LDO_TOP":  "28nm",
    "BANDGAP":  "28nm",
    "VCO_CORE": "16nm",
    "OTA_V3":   "28nm",
    "COMP_V1":  "16nm",
    "BIAS_GEN": "65nm",
    "DAC_8B":   "16nm",
}

# 构建 node_cells 字典:
# {
#   "28nm": ["LDO_TOP", "BANDGAP", "OTA_V3"],
#   "16nm": ["VCO_CORE", "COMP_V1", "DAC_8B"],
#   "65nm": ["BIAS_GEN"],
# }
# 然后:
#   (a) 打印每个 node 下的 cell 列表
#   (b) 找出使用最多的 node
#   (c) 把每个 node 下的 cell 名按字母排序

# >>> 在这里写代码 <<<


# ============================================================
# 练习 10: 解析复杂仿真 log 到嵌套字典
# ============================================================
# 一份典型的多 corner 仿真 log（每段对应一个 corner）

multi_corner_log = """
[corner: tt_25c]
gain    = 45.67
pm      = 62.30
gbw     = 125.8e6

[corner: ss_125c]
gain    = 38.21
pm      = 55.10
gbw     = 89.3e6

[corner: ff_m40c]
gain    = 52.04
pm      = 70.80
gbw     = 198.2e6
"""

# 解析成嵌套字典:
# {
#   "tt_25c":  {"gain": 45.67, "pm": 62.30, "gbw": 125800000.0},
#   "ss_125c": {"gain": 38.21, "pm": 55.10, "gbw": 89300000.0},
#   "ff_m40c": {"gain": 52.04, "pm": 70.80, "gbw": 198200000.0},
# }
# 提示:
#   1) splitlines() 按行处理
#   2) 遇到 [corner: xxx] 行，提取 corner 名，新建一个空 dict
#      可以用一个变量 current_corner 记住当前在哪个 corner 段
#   3) 遇到 key=value 行，存到 current_corner 对应的子字典里
#   4) 跳过空行
# 最后打印整个嵌套字典，并打印每个 corner 的 gain

# >>> 在这里写代码 <<<
