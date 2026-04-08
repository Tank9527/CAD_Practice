"""
Day 1 - Part 2: 字符串操作
场景：CAD 工程师最常用的操作 - 处理 cell name、路径、netlist 中的字符串
"""

# ============================================================
# 1. 字符串拼接与格式化
# ============================================================

lib = "myAnalogLib"
cell = "LDO_TOP"
view = "schematic"

# 方法 1: + 拼接（不推荐，慢且难读）
cell_path_v1 = lib + "/" + cell + "/" + view
print(f"方法1: {cell_path_v1}")

# 方法 2: f-string（推荐！Python 3.6+）
cell_path_v2 = f"{lib}/{cell}/{view}"
print(f"方法2: {cell_path_v2}")

# 方法 3: .format()
cell_path_v3 = "{}/{}/{}".format(lib, cell, view)
print(f"方法3: {cell_path_v3}")

# 方法 4: join（拼接列表中的字符串）
cell_path_v4 = "/".join([lib, cell, view])
print(f"方法4: {cell_path_v4}")

# 格式化数字（仿真结果显示）
gain = 42.567891
phase_margin = 65.3
print(f"\nGain = {gain:.2f} dB")          # 保留2位小数
print(f"PM = {phase_margin:.1f} deg")      # 保留1位小数
print(f"BW = {1.234e8:.2e} Hz")            # 科学计数法
print(f"Run {3:03d}")                       # 补零: Run 003

# ============================================================
# 2. 字符串常用方法
# ============================================================

# --- 大小写 ---
cell_name = "nmos_3p3_hvt"
print(f"\n原始: {cell_name}")
print(f"大写: {cell_name.upper()}")        # NMOS_3P3_HVT
print(f"小写: {cell_name.lower()}")        # nmos_3p3_hvt
print(f"首字母大写: {cell_name.title()}")  # Nmos_3P3_Hvt

# --- 查找与判断 ---
netlist_line = ".subckt LDO_TOP VIN VOUT VSS VREF"

print(f"\n分析 netlist 行: '{netlist_line}'")
print(f"是否以 .subckt 开头: {netlist_line.startswith('.subckt')}")
print(f"是否包含 VIN: {'VIN' in netlist_line}")
print(f"VIN 的位置: {netlist_line.find('VIN')}")  # 返回索引，找不到返回 -1
print(f"VOUT 的位置: {netlist_line.index('VOUT')}")  # 找不到会报错

# --- 替换 ---
old_param = "wp=2u wn=1u L=180n"
new_param = old_param.replace("180n", "150n")
print(f"\n替换前: {old_param}")
print(f"替换后: {new_param}")

# --- 分割与合并（最常用！）---
# split: 字符串 -> 列表
pin_line = "VIN VOUT VSS VDD VREF"
pins = pin_line.split()   # 按空格分割
print(f"\nPin 列表: {pins}")
print(f"Pin 数量: {len(pins)}")

# 按特定分隔符分割
cell_path = "myLib/LDO_TOP/schematic"
parts = cell_path.split("/")
print(f"路径分割: {parts}")
print(f"Library: {parts[0]}, Cell: {parts[1]}, View: {parts[2]}")

# join: 列表 -> 字符串
pins_csv = ", ".join(pins)
print(f"CSV 格式: {pins_csv}")

# --- 去除空白 ---
messy_line = "   gain = 42.5 dB   \n"
clean_line = messy_line.strip()
print(f"\n清理前: '{messy_line}'")
print(f"清理后: '{clean_line}'")

# ============================================================
# 3. 字符串切片（索引）
# ============================================================

cell_id = "NMOS_3P3_HVT_V2"

# 索引: 从 0 开始
print(f"\n字符串: {cell_id}")
print(f"第1个字符: {cell_id[0]}")       # N
print(f"最后1个字符: {cell_id[-1]}")     # 2
print(f"前4个字符: {cell_id[:4]}")       # NMOS
print(f"最后2个字符: {cell_id[-2:]}")    # V2
print(f"跳过前5个: {cell_id[5:]}")       # 3P3_HVT_V2

# 实用: 提取版本号
version = cell_id.split("_")[-1]        # 按 _ 分割取最后一个
print(f"版本: {version}")

# ============================================================
# 4. 实战：解析 Spectre netlist 行
# ============================================================

print("\n" + "="*50)
print("实战：解析 netlist")
print("="*50)

# 一行典型的 Spectre instance 描述
instance_line = "I0 (net1 net2 VDD VSS) nmos_3p3 w=2u l=180n m=4"

# 提取 instance 名
inst_name = instance_line.split()[0]
print(f"Instance: {inst_name}")

# 提取 pin 连接 (括号内的内容)
start = instance_line.index("(") + 1
end = instance_line.index(")")
nets = instance_line[start:end].split()
print(f"Nets: {nets}")

# 提取 cell name
after_paren = instance_line[end+2:]   # 跳过 ") "
cell_and_params = after_paren.split()
cell_model = cell_and_params[0]
print(f"Model: {cell_model}")

# 提取参数 (w, l, m)
params = {}
for item in cell_and_params[1:]:
    key, value = item.split("=")
    params[key] = value
print(f"Params: {params}")


# ============================================================
# 【练习题】请在下方写代码
# ============================================================

# 练习 1: 路径处理
# 给定以下信息，用 f-string 拼出完整的仿真目录路径
# 格式: /proj/{project}/user/{username}/sim/{cell}/{corner}/run_{run_id:03d}
project = "tape_out_2024"
username = "josn"
cell = "LDO_TOP"
corner = "tt_25c"
run_id = 7
# 期望输出: /proj/tape_out_2024/user/josn/sim/LDO_TOP/tt_25c/run_007

# >>> 在这里写代码 <<<
print(f"/proj/{project}/user/{username}/sim/{cell}/{corner}/run_{run_id:03d}")


# 练习 2: 解析 HSPICE 结果行
# 从下面的字符串中提取 gain 和 pm 的数值（浮点数）
hspice_result = "  gain=45.67dB   pm=62.30deg   gbw=125.8MHz"
# 提示:
#   1) 先 strip() 去空白
#   2) 用 split() 分割
#   3) 遍历每个 token，用 split("=") 分出 key 和 value
#   4) value 中去掉单位（用 replace 或切片）
# 期望: gain = 45.67, pm = 62.30

# >>> 在这里写代码 <<<
hspice_result_tmp = hspice_result.strip().split()
for kv in hspice_result_tmp[0:2]:
    key, value = kv.split("=")
    if key == "gain":
        print(f"{key} = {value[:-2]}")
    elif key == "pm":
        print(f"{key} = {value[:-3]}")


# 练习 3: Cell name 命名规则检查
# 检查一个 cell name 是否符合命名规范:
#   - 只能包含 小写字母、数字、下划线
#   - 必须以小写字母开头
#   - 长度在 3-30 之间
# 提示: str.isalnum(), str.islower(), str.startswith() 等方法
# 测试: "ldo_top_v2" -> OK, "3LDO" -> 不合法, "a" -> 太短

test_names = ["ldo_top_v2", "3LDO", "a", "LDO_TOP", "nmos_3p3_hvt", "my cell"]

# >>> 在这里写代码（遍历 test_names 逐个检查）<<<
for name in test_names:
    if (3 <= len(name) <= 30 and
        name[0].islower() and
        all(c.islower() or c.isdigit() or c == '_' for c in name)):
        print(f"{name} -> 合法")
    else:
        print(f"{name} -> 不合法")

