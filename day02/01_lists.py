"""
Day 2 - Part 1: 列表 (List)
场景：CAD 工程师用列表管理 corner、cell、仿真结果等批量数据
"""

# ============================================================
# 1. 创建列表
# ============================================================

# 空列表
corners = []

# 直接初始化
cells = ["LDO_TOP", "BANDGAP", "VCO_CORE", "OTA_V2", "BIAS_GEN"]
voltages = [1.62, 1.8, 1.98]
drc_results = [True, True, False, True, False]

print(f"Cell 列表: {cells}")
print(f"长度: {len(cells)}")

# ============================================================
# 2. 索引与切片（和字符串类似）
# ============================================================

print(f"\n第1个 cell: {cells[0]}")
print(f"最后1个 cell: {cells[-1]}")
print(f"前3个 cell: {cells[:3]}")
print(f"倒数2个 cell: {cells[-2:]}")

# 修改元素（字符串不能改，列表可以！）
cells[3] = "OTA_V3"    # 把 OTA_V2 升级到 V3
print(f"升级后: {cells}")

# ============================================================
# 3. 常用方法
# ============================================================

# --- 增 ---
cells.append("COMP_V1")           # 末尾添加
print(f"\nappend 后: {cells}")

cells.insert(0, "TOP_CHIP")       # 指定位置插入
print(f"insert 后: {cells}")

more_cells = ["DAC_8B", "ADC_12B"]
cells.extend(more_cells)           # 合并另一个列表
print(f"extend 后: {cells}")

# --- 删 ---
cells.remove("COMP_V1")           # 按值删除（只删第一个匹配）
print(f"\nremove 后: {cells}")

popped = cells.pop()               # 弹出最后一个，返回被删的值
print(f"pop 出: {popped}, 剩余: {cells}")

popped2 = cells.pop(0)             # 弹出指定位置
print(f"pop(0) 出: {popped2}, 剩余: {cells}")

# --- 查 ---
print(f"\nBANDGAP 在列表中? {'BANDGAP' in cells}")
print(f"BANDGAP 的索引: {cells.index('BANDGAP')}")
print(f"LDO_TOP 出现次数: {cells.count('LDO_TOP')}")

# --- 排序 ---
gain_values = [42.5, 38.2, 52.1, 36.8, 45.7]
gain_values.sort()                  # 原地排序（改变原列表）
print(f"\n升序: {gain_values}")

gain_values.sort(reverse=True)     # 降序
print(f"降序: {gain_values}")

# sorted() 不改变原列表，返回新列表
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(f"原列表: {original}, sorted 结果: {new_sorted}")

# ============================================================
# 4. 列表推导式（List Comprehension）
# ============================================================
# 这是 Python 最强大的特性之一，CAD 脚本里大量使用

# 基本语法: [表达式 for 变量 in 可迭代对象]
corners = [f"corner_{i}" for i in range(5)]
print(f"\n生成 corners: {corners}")

# 带条件过滤: [表达式 for 变量 in 可迭代对象 if 条件]
gains = [42.5, 38.2, 52.1, 36.8, 45.7, 33.0, 48.9]
good_gains = [g for g in gains if g >= 40.0]
print(f"增益 >= 40dB 的: {good_gains}")

# 对每个元素做转换
cell_names = ["ldo_top", "bandgap", "vco_core"]
upper_names = [name.upper() for name in cell_names]
print(f"大写: {upper_names}")

# 实战: 从 corner 名提取温度
corner_list = ["tt_25c", "ss_125c", "ff_m40c", "ss_m40c"]
temps = [c.split("_")[1].replace("c", "") for c in corner_list]
print(f"温度: {temps}")

# ============================================================
# 5. 遍历技巧
# ============================================================

cells = ["LDO_TOP", "BANDGAP", "VCO_CORE"]

# enumerate: 同时拿到索引和值
print("\n--- enumerate ---")
for i, cell in enumerate(cells):
    print(f"  [{i}] {cell}")

# zip: 并行遍历多个列表
gains = [45.67, 38.21, 52.04]
pms = [62.3, 55.1, 70.8]

print("\n--- zip ---")
for cell, gain, pm in zip(cells, gains, pms):
    print(f"  {cell}: Gain={gain}dB, PM={pm}deg")

# ============================================================
# 6. 嵌套列表（二维数据）
# ============================================================

# 仿真结果表: 每行 = [corner, gain, pm, gbw]
sim_table = [
    ["tt_25c",  45.67, 62.3, 125.8],
    ["ss_125c", 38.21, 55.1,  89.3],
    ["ff_m40c", 52.04, 70.8, 198.2],
]

print(f"\n第2行: {sim_table[1]}")
print(f"第2行的 gain: {sim_table[1][1]}")

# 提取所有 gain 值（取每行的第2列）
all_gains = [row[1] for row in sim_table]
print(f"所有 gain: {all_gains}")
print(f"最大 gain: {max(all_gains):.2f} dB")
print(f"最小 gain: {min(all_gains):.2f} dB")


# ============================================================
# 【练习题】请在下方写代码
# ============================================================

# 练习 1: Pin 列表操作
# 从 netlist 的 .subckt 行提取 pin 列表，然后做以下操作
subckt_line = ".subckt LDO_TOP VIN VOUT VFB VREG VSS VDD EN"
# (a) 提取所有 pin 名到列表（跳过 .subckt 和 cell name）
# (b) 打印 pin 总数
# (c) 检查 "VSS" 是否在 pin 列表中
# (d) 把 pin 列表按字母排序后打印
# (e) 在 "EN" 后面添加一个新 pin "TRIM"，打印结果

# >>> 在这里写代码 <<<
line_split = subckt_line.split() #把字符串按空格分成列表，得到[".subckt","LDO_TOP","VIN","VOUT","VFB","VREG","VSS","VDD","EN"]
pin_list = line_split[2:] #从索引2开始切片，得到["VIN","VOUT","VFB","VREG","VSS","VDD","EN"]  
print(f"Pin列表: {pin_list},总数: {len(pin_list)}") #len()函数计算列表长度，即pin数量
if "VSS" in pin_list:
    print(f"VSS在pin列表中")
print(f"{sorted(pin_list)}") #sorted()函数返回一个新的排序后的列表，原列表不变
pin_list.append("TRIM")
print(f"{pin_list.append("TRIM")}")


# 练习 2: 列表推导式训练
# (a) 用列表推导式生成 1-20 中所有偶数的平方: [4, 16, 36, ...]
# (b) 给定仿真增益列表，找出低于 spec (40dB) 的 corner
sim_data = [
    ("tt_25c", 45.67),
    ("ss_125c", 38.21),
    ("ff_m40c", 52.04),
    ("ss_m40c", 36.88),
    ("ff_125c", 41.05),
]
# 用列表推导式提取 gain < 40 的 corner 名
# 期望: ["ss_125c", "ss_m40c"]

# >>> 在这里写代码 <<<
print([x**2 for x in range(1,21) if x % 2 == 0]) #生成1-20中所有偶数的平方
print([f"小于40dB的{corner} : {dB}dB" for corner, dB in sim_data if dB < 40]) #提取gain < 40的corner名和对应的gain值

# 练习 3: 仿真结果分析
# 给定多组仿真数据，找出每个指标的 best/worst corner
results = [
    ("tt_25c",  45.67, 62.3, 125.8),
    ("ss_125c", 38.21, 55.1,  89.3),
    ("ff_m40c", 52.04, 70.8, 198.2),
    ("ss_m40c", 36.88, 51.2,  75.6),
    ("ff_125c", 41.05, 58.9, 145.0),
]
# 格式: (corner, gain, pm, gbw)
# 找出并打印:
#   Gain  最大的 corner 和值
#   Gain  最小的 corner 和值
#   PM    最小的 corner 和值（PM 最小 = worst）
#   GBW   最小的 corner 和值（GBW 最小 = worst）
# 提示: 可以用 max()/min() 配合 key 参数，或者用列表推导式

# >>> 在这里写代码 <<<
print([f"best corner: {corner}" for corner, gain, pm, gbw in results if gain == max([r[1] for r in results])]) #找出gain最大的corner和对应的gain值
print([f"worst corner: {corner}" for corner, gain, pm, gbw in results if gain == min([r[1] for r in results])]) #找出gain最小的corner和对应的gain值
print([f"worst corner: {corner}" for corner, gain, pm, gbw in results if pm == min([r[2] for r in results])]) #找出pm最小的corner和对应的pm值
print([f"worst corner: {corner}" for corner, gain, pm, gbw in results if gbw == min([r[3] for r in results])]) #找出gbw最小的corner和对应的gbw值


# 练习 4: 合并去重排序
# 两个工程师各自跑了一些 corner，合并后去重并排序
josn_corners = ["tt_25c", "ss_125c", "ff_m40c", "tt_m40c"]
mike_corners = ["tt_25c", "ff_125c", "ss_m40c", "ss_125c", "ff_m40c"]
# (a) 合并两个列表
# (b) 去掉重复的 corner（提示: 可以用 set() 或循环判断）
# (c) 按字母排序
# (d) 打印最终列表和总数
# 期望: ['ff_125c', 'ff_m40c', 'ss_125c', 'ss_m40c', 'tt_25c', 'tt_m40c'] 共 6 个

# >>> 在这里写代码 <<<
extend_corners = josn_corners.extend(mike_corners) #合并两个列表，修改josn_corners，返回值是None，所以extend_corners的值是None
unique_corners = list(set(josn_corners)) #用set()去重，再用list()把set转换回列表
sorted_corners = sorted(unique_corners) #用sorted()排序，返回一个新的列表，原列表不变
print(f"最终列表: {sorted_corners}, 总数: {len(sorted_corners)}")