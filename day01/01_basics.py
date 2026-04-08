"""
Day 1 - Part 1: 变量与数据类型
场景：模拟 CAD 工程师日常接触的基本数据
"""

# ============================================================
# 1. 基本数据类型
# ============================================================

# 字符串 str - cell name, lib name
lib_name = "analogLib"
cell_name = "nmos_3p3"
view_name = "schematic"

# 整数 int - 仿真次数、corner 数量
num_corners = 27
num_monte_carlo = 1000

# 浮点数 float - 电气参数
vdd = 1.8
temperature = 25.0
threshold_voltage = 0.45

# 布尔值 bool - 状态标志
sim_passed = True
drc_clean = False

# 查看类型用 type()
print(f"lib_name 的类型: {type(lib_name)}")
print(f"num_corners 的类型: {type(num_corners)}")
print(f"vdd 的类型: {type(vdd)}")
print(f"sim_passed 的类型: {type(sim_passed)}")

# ============================================================
# 2. 类型转换
# ============================================================

# 从 log 里读出来的数值通常是字符串，需要转换
gain_str = "42.5"         # 从 log 中读到的增益值
gain_float = float(gain_str)
print(f"\n增益: {gain_float} dB (类型: {type(gain_float)})")

corner_str = "27"
corner_int = int(corner_str)
print(f"Corner 数: {corner_int}")

# 数字转字符串（拼接文件名时常用）
run_id = 5
run_dir = "run_" + str(run_id)
print(f"运行目录: {run_dir}")

# ============================================================
# 3. 数学运算
# ============================================================

# 常用电路计算
r1 = 10e3   # 10kΩ  (科学计数法)
r2 = 20e3   # 20kΩ
c1 = 1e-12  # 1pF

# 并联电阻
r_parallel = (r1 * r2) / (r1 + r2)
print(f"\n并联电阻: {r_parallel:.2f} Ω")

# RC 时间常数
tau = r_parallel * c1
print(f"RC 时间常数: {tau:.4e} s")

# 带宽
import math
bw = 1 / (2 * math.pi * tau)
print(f"-3dB 带宽: {bw:.2f} Hz = {bw/1e6:.2f} MHz")

# 整除和取余（计算需要多少批次跑仿真）
total_sims = 1000
batch_size = 64
num_batches = total_sims // batch_size   # 整除
remaining = total_sims % batch_size       # 取余
print(f"\n总仿真 {total_sims} 次, 每批 {batch_size} 次")
print(f"需要 {num_batches} 个完整批次 + {remaining} 次剩余")


# ============================================================
# 【练习题】请在下方写代码
# ============================================================

# 练习 1: 定义以下变量
# - process_node: 工艺节点字符串，值为 "28nm"
# - supply_voltage: 电源电压，值为 0.9
# - metal_layers: 金属层数，值为 8
# - is_finfet: 是否是 FinFET 工艺，值为 False
# 然后打印出: "工艺: 28nm, VDD=0.9V, 8层金属, FinFET: False"

# >>> 在这里写代码 <<<
#工艺节点字符串
process_node = '28nm'
print(f'工艺节点：{process_node}')

supply_voltage = 0.9
print(f'电源电压：{supply_voltage}')

metal_layers = 8
print(f'金属层数:{metal_layers}')

is_finfet = False
print(f'是否是FINFET工艺:{is_finfet}')

print(f'工艺:{process_node},VDD={supply_voltage}V,{metal_layers}层金属,FINFET:{is_finfet}')

# 练习 2: 电路计算
# 已知 gm = 1e-3 (跨导), rout = 50e3 (输出电阻), CL = 2e-12 (负载电容)
# 计算: (1) 增益 Av = gm * rout
#       (2) 增益 dB = 20 * log10(Av)  提示: math.log10()
#       (3) GBW = gm / (2 * pi * CL)
# 打印结果

# >>> 在这里写代码 <<<
gm = 1e-3
rout = 50e3
CL = 2e-12
import math
#(1)
Av = gm * rout
#(2)
dB = 20 * math.log10(Av)
#(3)
GBW = gm / (2 * math.pi * CL)
print(f'增益Av:{Av}\n增益dB:{dB}\nGBW={GBW}')

# 练习 3: 类型转换
# 下面是从仿真 log 中 "读取" 到的字符串，请转换并计算
power_str = "2.35e-3"     # 功耗 (W)
current_str = "1.306e-3"  # 电流 (A)
voltage_str = "1.8"       # 电压 (V)
# 计算: 验证 P = V * I 是否约等于 power_str 的值
# 提示: 用 abs(a - b) < 1e-6 判断两个浮点数是否近似相等

# >>> 在这里写代码 <<<
if abs(float(voltage_str) * float(current_str) - float(power_str)) < 1e-6:
    print(f'P = V * I,验证通过')
else:
    print(f'P!= V * I,差值{abs(float(voltage_str) * float(current_str) - float(power_str))}')