# Day 01 变量/字符串练习 - 错误总结与改进建议

> 注: Day 01 的聊天记录不可回溯,以下内容从代码中分析得出。

## 一、01_basics.py 练习中的问题

### 练习 1: 重复打印

**你的写法:**
```python
print(f'工艺节点：{process_node}')
print(f'电源电压：{supply_voltage}')
print(f'金属层数:{metal_layers}')
print(f'是否是FINFET工艺:{is_finfet}')
print(f'工艺:{process_node},VDD={supply_voltage}V,{metal_layers}层金属,FINFET:{is_finfet}')
```

**问题:** 题目要求打印一行,前面四行多余了。不是错误,但说明没仔细读题目要求的输出格式。

### 练习 2: import 位置 + 变量命名

```python
# 第 70 行已经 import math
import math     # 第 121 行又 import 了一次
Av = gm * rout  # 大写开头的变量名
CL = 2e-12
GBW = gm / (2 * math.pi * CL)
```

**问题:**
1. `import math` 写了两次。Python 不会报错(第二次是空操作),但 `import` 应集中放在文件**最顶部**,这是 PEP 8 规范。
2. `Av`、`CL`、`GBW` 用了大写开头——PEP 8 约定大写开头是类名(`class MyClass`),变量用全小写+下划线(`av`、`c_load`、`gbw`)。在 EDA 领域这些是常见缩写,大写有一定合理性,但在 Python 社区会被 linter 标黄。

### 练习 3: 重复计算

```python
if abs(float(voltage_str) * float(current_str) - float(power_str)) < 1e-6:
    print(f'P = V * I,验证通过')
else:
    print(f'P!= V * I,差值{abs(float(voltage_str) * float(current_str) - float(power_str))}')
```

**问题:** `float(voltage_str) * float(current_str)` 和 `float(power_str)` 各算了**两遍**(if 里一遍,else 里又一遍)。应该先存变量:

```python
p_calc = float(voltage_str) * float(current_str)
p_expected = float(power_str)
diff = abs(p_calc - p_expected)

if diff < 1e-6:
    print("P = V * I, 验证通过")
else:
    print(f"P != V * I, 差值 {diff}")
```

**好处:** 改一个地方就够,不容易漏改;也更好读。

---

## 二、02_strings.py 练习中的问题

### 练习 2: 硬编码去单位

```python
for kv in hspice_result_tmp[0:2]:
    key, value = kv.split("=")
    if key == "gain":
        print(f"{key} = {value[:-2]}")     # 砍掉最后 2 个字符 "dB"
    elif key == "pm":
        print(f"{key} = {value[:-3]}")     # 砍掉最后 3 个字符 "deg"
```

**问题:**
1. 每个 key 对应的单位长度不同(`dB` 2 个字符,`deg` 3 个字符,`MHz` 3 个字符),需要 if/elif 逐个硬编码。加一种单位就要加一个分支。
2. 只处理了前 2 个 token(`[0:2]`),`gbw` 被丢掉了。
3. 提取出来的值还是字符串,没有转成 float。

**更通用的写法:**
```python
# 用 strip() 去掉非数字字符(字母),或者用简单规则:
# 从右边找到第一个数字的位置,前面的是数值,后面的是单位
for token in hspice_result.strip().split():
    key, raw_value = token.split("=")
    # 把尾部的字母去掉,只留数字部分
    i = len(raw_value)
    while i > 0 and raw_value[i-1].isalpha():
        i -= 1
    value = float(raw_value[:i])
    unit = raw_value[i:]
    print(f"{key} = {value} {unit}")
```

以后学正则表达式(Day 6)后可以更优雅地解决。

---

## 三、02_strings_extra.py 练习中的问题

### 练习 6: 多余的初始化 + 长行

```python
path_info_list = []           # ← 多余,下一行就被覆盖了
for path in sim_paths:
    path_info_list = path.split("/")
    print(f"Project: {path_info_list[2]} | User: {path_info_list[4]} | Cell: {path_info_list[6]} | Corner: {path_info_list[7]} | Run: {int(path_info_list[8].split('_')[1])}")
```

**问题:**
1. `path_info_list = []` 初始化没用——进入循环后立刻被 `path.split("/")` 覆盖。
2. print 那一行太长,不好读。可以用解包让代码更清晰:

```python
for path in sim_paths:
    _, _, proj, _, user, _, cell, corner, run_dir, _ = path.split("/")
    run_num = int(run_dir.split("_")[1])
    print(f"Project: {proj} | User: {user} | Cell: {cell} | Corner: {corner} | Run: {run_num}")
```

### 练习 7: Netlist 注释清理 - 原始 bug 与修复

**原始代码(已注释掉)的 bug:**
```python
# else:
#     netlist_pure.append(line.strip())  # ← 把带 // 注释的整行都加进去了
```
没有处理行内注释 `R0 VIN net1 10k   // feedback resistor`。

**修复后的代码:**
```python
if "//" in line:
    netlist_pure.append(line.split("//")[0].strip())
else:
    netlist_pure.append(line.strip())
```

修复正确。但注意这两个分支的结构可以**合并简化**:

```python
for line in raw_netlist.split('\n'):
    line = line.split("//")[0].strip()   # 先砍掉 // 及后面的部分,再 strip
    if line.startswith("*") or line == "":
        continue
    netlist_pure.append(line)
```

思路: **不管有没有 `//`,都先 `split("//")[0]`** —— 没有 `//` 时 split 返回 `[整行]`,取 `[0]` 就是原行,不影响结果。这样就不需要 if/else 分两种情况了。

### 练习 9: 分隔线硬编码(同 Day 02)

```python
print("-" * 15 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 15)
```

**同样的问题:** 改列宽就得手动重算。改成 `len(header)` 的方式更稳妥(Day 02 总结已详细说明)。

---

## 四、Day 01 做得好的地方

### 练习 3 (01_basics.py): 浮点数比较
```python
abs(float(voltage_str) * float(current_str) - float(power_str)) < 1e-6
```
知道浮点数不能用 `==` 直接比较,用 `abs(a - b) < epsilon` 判断近似相等。

### 练习 8 (02_strings_extra.py): 版本号比较
```python
v1_split = list(map(int, v1[1:].split('.')))
v2_split = list(map(int, v2[1:].split('.')))
if v1_split < v2_split:
```
- `map(int, ...)` 批量转换类型
- 利用 Python 列表的**逐元素比较**特性,一行搞定版本号大小比较
- 这个写法很 Pythonic

### 练习 7: 自己发现 bug 并修复
从注释掉的原始代码和修复后的代码可以看出,自己跑完发现行内注释没清掉,独立修复了问题。

### 练习 4 (02_strings_extra.py): Spectre 参数解析
```python
param_list = param_line.split()[1:]   # 跳过 "parameters" 关键字
for param in param_list:
    key, value = param.split("=")
    expected_dict[key] = float(value)
```
干净利落,注释也到位。

---

## 五、Day 01 涉及的语法知识点

从代码和注释中可以看出已掌握的知识:

| 知识点 | 在哪里用到 |
|--------|-----------|
| f-string 格式化 (`:.2f`, `:03d`, `:.2e`) | 练习 1/2/9 |
| `split()` / `split("=")` / `split("/")` | 练习 2/4/6 |
| `strip()` 去首尾空白 | 练习 2/7 |
| `startswith()` 判断前缀 | 练习 7 |
| 列表切片 `[1:]` / `[:5]` / `[:-2]` | 练习 2/4/5 |
| `continue` 跳过循环 | 练习 7 |
| `map(int, ...)` 批量类型转换 | 练习 8 |
| 列表的逐元素比较 `[1,2] < [1,3]` | 练习 8 |
| `float()` / `int()` 类型转换 | 练习 3/6 |
| 三层嵌套 for 循环 | 练习 5 |
| `split("/")` 第一个元素是空串(路径以 `/` 开头) | 练习 6 注释 |
| `all()` + 生成器表达式 | 练习 3 命名规则检查 |
