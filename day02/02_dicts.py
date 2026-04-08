"""
Day 2 - Part 2: 字典 (Dict)
场景：CAD 工程师用字典管理参数、配置、查找表 — 这是 flow 脚本里最常用的数据结构
"""

# ============================================================
# 1. 创建字典
# ============================================================

# 字典是 key-value 对的集合，用 {} 创建
# key 必须是不可变类型（字符串、数字、tuple），value 任意

# 一个 MOSFET 器件参数
nmos_params = {
    "model": "nmos_3p3",
    "w": 2e-6,
    "l": 180e-9,
    "m": 4,
    "vth": 0.45,
}

print(f"器件参数: {nmos_params}")
print(f"参数个数: {len(nmos_params)}")

# 空字典
empty_dict = {}
empty_dict2 = dict()    # 等价写法

# ============================================================
# 2. 访问与修改
# ============================================================

# 用 [key] 访问
print(f"\nW = {nmos_params['w']}")
print(f"L = {nmos_params['l']}")

# 用 [key] 赋值（如果 key 不存在则新增）
nmos_params["w"] = 4e-6           # 修改 w
nmos_params["nf"] = 2              # 新增 nf (number of fingers)
print(f"修改后: {nmos_params}")

# 用 .get() 安全访问 — 不存在不会报错，返回 None 或默认值
print(f"\nvds: {nmos_params.get('vds')}")              # None
print(f"vds: {nmos_params.get('vds', 1.8)}")           # 1.8 (默认值)

# 直接 [key] 访问不存在的 key 会 KeyError
# print(nmos_params["vds"])   # KeyError!

# 检查 key 是否存在
print(f"\n'w' 在字典中? {'w' in nmos_params}")
print(f"'vds' 在字典中? {'vds' in nmos_params}")

# ============================================================
# 3. 删除
# ============================================================

# del 删除
del nmos_params["nf"]
print(f"\n删除 nf 后: {nmos_params}")

# pop 删除并返回值
popped = nmos_params.pop("vth")
print(f"pop 出 vth = {popped}")

# pop 加默认值，避免 key 不存在时报错
val = nmos_params.pop("vds", None)
print(f"pop vds = {val}")

# ============================================================
# 4. 遍历字典
# ============================================================

config = {
    "vdd": 1.8,
    "temp": 25,
    "corner": "tt",
    "sim_time": 100e-9,
}

# 遍历 keys（默认行为）
print("\n--- 遍历 keys ---")
for key in config:
    print(f"  {key}")

# 遍历 values
print("\n--- 遍历 values ---")
for value in config.values():
    print(f"  {value}")

# 遍历 key-value 对（最常用！）
print("\n--- 遍历 items ---")
for key, value in config.items():
    print(f"  {key} = {value}")

# ============================================================
# 5. 字典推导式
# ============================================================

# 和列表推导式语法类似，但用 {} 且需要 key:value
# 把 corner 列表转成 corner -> 索引的查找表
corners = ["tt_25c", "ss_125c", "ff_m40c", "ss_m40c"]
corner_idx = {name: i for i, name in enumerate(corners)}
print(f"\nCorner 索引表: {corner_idx}")

# 翻转 key-value
flipped = {v: k for k, v in corner_idx.items()}
print(f"翻转后: {flipped}")

# 带条件过滤
gains = {"tt_25c": 45.67, "ss_125c": 38.21, "ff_m40c": 52.04, "ss_m40c": 36.88}
good = {k: v for k, v in gains.items() if v >= 40.0}
print(f"达标的: {good}")

# ============================================================
# 6. 嵌套字典（实际工作中最常见）
# ============================================================

# 多个 cell 各自的参数表
cell_db = {
    "LDO_TOP": {
        "type": "analog",
        "owner": "josn",
        "version": "v1.2.3",
        "pins": ["VIN", "VOUT", "VSS"],
    },
    "BANDGAP": {
        "type": "analog",
        "owner": "mike",
        "version": "v2.0.1",
        "pins": ["VREF", "VDD", "VSS"],
    },
}

# 访问嵌套字段
print(f"\nLDO_TOP 的 owner: {cell_db['LDO_TOP']['owner']}")
print(f"BANDGAP 的 pins: {cell_db['BANDGAP']['pins']}")

# 遍历嵌套字典
print("\n--- 所有 cell 的版本 ---")
for cell_name, info in cell_db.items():
    print(f"  {cell_name}: {info['version']} (owner: {info['owner']})")

# ============================================================
# 7. 实战：解析 Spectre 参数行到字典
# ============================================================

print("\n" + "="*50)
print("实战：参数行 -> 字典")
print("="*50)

param_line = "M0 (d g s b) nmos_3p3 w=2u l=180n m=4 nf=2"

tokens = param_line.split()
inst_name = tokens[0]
model = tokens[5]                  # 跳过括号内的 4 个 net
params = {}
for token in tokens[6:]:
    key, value = token.split("=")
    params[key] = value

print(f"Instance: {inst_name}")
print(f"Model:    {model}")
print(f"Params:   {params}")


# ============================================================
# 【练习题】请在下方写代码
# ============================================================

# 练习 1: 器件参数字典
# 创建一个 PMOS 器件的参数字典，包含:
#   model = "pmos_3p3", w = 4e-6, l = 180e-9, m = 2, vth = -0.4
# 然后:
#   (a) 把 m 改成 8
#   (b) 添加一个新参数 nf = 4
#   (c) 用 .get() 尝试取 "vds"，给默认值 1.8
#   (d) 删除 "vth"
#   (e) 打印最终字典和所有 key 的列表

# >>> 在这里写代码 <<<
pmos_dict = {"model": "pmos_3p3", "w": 4e-6, "l": 180e-9, "m": 2, "vth": -0.4} #创建PMOS器件参数字典
pmos_dict["m"] = 8 #把m改成8
pmos_dict["nf"] = 4 #添加新参数nf=4
print(pmos_dict.get("vds", 1.8)) #用.get()尝试取"vds"，给默认值1.8
del pmos_dict["vth"] #删除"vth"
print(f"最终字典: {pmos_dict}, 所有key的列表: {list(pmos_dict.keys())}") #打印最终字典和所有key的列表

# 练习 2: Corner 结果查表
# 给定 gain 字典，用字典推导式做几件事
gain_dict = {
    "tt_25c":  45.67,
    "ss_125c": 38.21,
    "ff_m40c": 52.04,
    "ss_m40c": 36.88,
    "ff_125c": 41.05,
    "tt_m40c": 43.20,
}
# (a) 用字典推导式，把所有 gain 加 0.5dB（模拟校准）
# (b) 用字典推导式，筛选出 gain >= 40 的 corner
# (c) 找出 gain 最大的 corner 名（提示: max(dict, key=dict.get)）
# (d) 打印字典中所有 gain 的平均值

# >>> 在这里写代码 <<<
new_gain = {corner: gain+0.5 for corner, gain in gain_dict.items()}
new_gain1 = {corner: gain for corner, gain in gain_dict.items() if gain >= 40}
max_gain = max(gain_dict, key=gain_dict.get) #找出gain最大的corner名，max函数的key参数指定了比较的依据，这里是字典的get方法，即比较每个corner对应的gain值
for corner, gain in gain_dict.items():
    if corner == max_gain:
        print(f"gain最大的corner: {corner}, gain = {gain}dB") #打印gain最大的corner名和对应的gain值
average_gain = sum(gain_dict.values()) / len(gain_dict) #计算所有gain的平均值，sum函数计算所有gain的总和，len函数计算corner的数量
print(f"平均值gain: {average_gain:.2f}dB")

# 练习 3: Cell 数据库查询
# 用嵌套字典维护 cell 信息
cell_db = {
    "LDO_TOP":  {"owner": "josn", "version": "v1.2.3", "status": "released"},
    "BANDGAP":  {"owner": "mike", "version": "v2.0.1", "status": "released"},
    "VCO_CORE": {"owner": "josn", "version": "v0.9.5", "status": "WIP"},
    "OTA_V3":   {"owner": "alice","version": "v1.0.0", "status": "released"},
    "COMP_V1":  {"owner": "mike", "version": "v0.5.2", "status": "WIP"},
}
# (a) 打印所有 owner 是 "josn" 的 cell 名
# (b) 统计 status 为 "released" 和 "WIP" 的 cell 数量
# (c) 给所有 cell 添加一个新字段 "lib": "myAnalogLib"
# (d) 找出 owner 为 "mike" 且 status 为 "released" 的所有 cell

# >>> 在这里写代码 <<<
for cell_name, info in cell_db.items():
    if info["owner"] == "josn":
        print(f"owner是josn的cell: {cell_name}") #打印所有owner是"josn"的cell名

released_count = sum(1 for info in cell_db.values() if info["status"] == "released") #统计status为"released"的cell数量，生成器表达式info for info in cell_db.values() if info["status"] == "released"会遍历cell_db字典的所有值（即每个cell的信息字典），满足条件的info会被sum()函数累加
wip_count = sum(1 for info in cell_db.values() if info["status"] == "WIP") #统计status为"WIP"的cell数量，生成器表达式info for info in cell_db.values() if info["status"] == "WIP"会遍历cell_db字典的所有值（即每个cell的信息字典），满足条件的info会被sum()函数累加
print(f"relseased数量: {released_count}, WIP数量: {wip_count}") #打印status为"released"和"WIP"的cell数量
for info in cell_db.values():
    info["lib"] = "myAnalogLib" #给所有cell添加一个新字段"lib":"myAnalogLib"
for cell_name, info in cell_db.items():
    if info["owner"] == "mike" and info["status"] == "released":
        print(f"owner为mike且status为released的cell: {cell_name}") #找出owner为"mike"且status为"released"的所有cell名

# 练习 4: 解析 .measure 输出
# 从下面这段仿真 log 中提取所有 measure 结果到字典
measure_log = """
gain          =   45.67
pm            =   62.30
gbw           =   125.8e6
power         =   2.35e-3
vout_dc       =   0.900
"""
# 期望结果（值都是 float）:
# {"gain": 45.67, "pm": 62.3, "gbw": 125800000.0, "power": 0.00235, "vout_dc": 0.9}
# 提示:
#   1) splitlines() 按行分割
#   2) 每行 strip() 后跳过空行
#   3) split("=") 拿到 key 和 value
#   4) 都要 strip() 去空白，value 用 float() 转换

# >>> 在这里写代码 <<<
measure_splitlines = measure_log.splitlines() #按行分割，得到一个列表，每个元素是一行字符串
measure_dict = {}
for line in measure_splitlines:
    line_strip = line.strip() #去掉每行的空白字符
    if line_strip: #如果line_strip不为空字符串
        key, value = line_strip.split("=") #用"="分割拿到key和value，得到一个列表，在解包得到字典的key和value
        key = key.strip() #去掉key的空白字符
        value = float(value.strip()) #去掉value的空白字符并转换成float类型
        measure_dict[key] = value #把key和value添加到measure_dict字典中，key是字典的键，value是字典的值