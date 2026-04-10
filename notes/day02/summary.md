# Day 02 字典练习 - 错误总结与语法笔记

## 一、练习中犯的错误

### 练习 5(a): 打印 tt_25c 的 vth 值

**原始错误代码:**
```python
for value in pvt_table["tt_25c"].values():
    if value.key() == "vth":
        print(f"tt_25c的vth值: {value["vth"]}")
```

**问题清单:**

| # | 错误 | 原因 |
|---|------|------|
| 1 | `.values()` 返回的是 float,不是 dict | `{"vth": 0.45, ...}.values()` → `0.45, 320, 1.2e5`,都是数字 |
| 2 | float 没有 `.key()` 方法 | `.key()` 不是任何内置类型的方法,dict 的方法是 `.keys()` |
| 3 | f-string 双引号嵌套 `{value["vth"]}` | 外层 `f"..."` 和内层 `"vth"` 都用双引号,Python 3.12 以下报语法错 |
| 4 | 已知 key 还用循环遍历去找 | 直接 `d[key]` 取就行,循环是处理"不知道 key"的场景 |

**修改后仍存在的问题:**
```python
# 这行仍然有 bug:
print(f"tt_25c的vth值: {[value["vth"] for value in pvt_table["tt_25c"].values() if value.key() == "vth"][0]}")
```
- 仍然在 `.values()` 的 float 上调用 `.key()` 和 `["vth"]`
- 仍然有双引号嵌套问题
- 用列表推导式做了一件不需要推导式的事

**正确写法(一行):**
```python
print(f"tt_25c 的 vth = {pvt_table['tt_25c']['vth']}")
```

**核心教训:** 已知 key 直接用 `d[key]` 取值,不要绕弯子。搞清楚 `.keys()`/`.values()`/`.items()` 分别返回什么。

---

### 练习 5(b): 找 vth 最大的 corner

**原始写法:**
```python
for corner, params in pvt_table.items():
    if params["vth"] == max(pvt_table.values(), key=lambda x: x["vth"])["vth"]:
        print(f"vth最大的corner: {corner}, vth = {params['vth']}")
```

**问题:** 逻辑正确但低效且绕弯
- `max(...)` 放在循环的 `if` 里,每次循环都重新算一遍 max(3 个 corner → 算 3 次)
- `max()` 返回的是子 dict,丢失了 corner 名字,又得循环找回来

**改后方法 2 仍有 bug:**
```python
maxcorner, params = max(pvt_table.items(), key=lambda kv : kv[1]["vth"])
print(f"vth最大: {maxcorner} = {params[1]["vth"]}")
#                                     ↑ 错误!
```
- 解包后 `params` 已经是子 dict `{"vth": 0.52, ...}`,不再是元组
- `params[1]` 会 KeyError(dict 没有整数 key `1`)
- 应该写 `params["vth"]`

**正确写法:**
```python
# 方法 1: max 遍历 key,返回 corner 名
max_corner = max(pvt_table, key=lambda c: pvt_table[c]["vth"])
print(f"vth 最大: {max_corner} = {pvt_table[max_corner]['vth']}")

# 方法 2: max 遍历 items,解包后直接用
name, params = max(pvt_table.items(), key=lambda kv: kv[1]["vth"])
print(f"vth 最大: {name} = {params['vth']}")   # ← params 就是子 dict
```

**核心教训:** `max()` 能直接返回"最大的那个元素",让它遍历能唯一标识元素的东西(key 或 items),不要拿到值后再循环找 key。解包后的变量类型要想清楚。

---

### 练习 6: 按 owner 分组 cell

**原始错误代码:**
```python
cell_dict = {}
cell_list = []
for cell, onwer in cells_info:
    if onwer not in cell_dict.keys():
        cell_list.append(cell)
        cell_dict[onwer] = cell_list
    else:
        cell_list.append(cell)
        cell_dict[onwer] = cell_list
```

**问题清单:**

| # | 错误 | 原因 |
|---|------|------|
| 1 | **所有 owner 共享同一个 list**(核心 bug) | `cell_list` 在循环外只创建了一个,所有 `cell_dict[owner] = cell_list` 都指向同一个对象 |
| 2 | `if` / `else` 两个分支代码完全一样 | 判断了存不存在,但两边做一模一样的事,等于没判断 |
| 3 | `onwer` 拼写错误 | 应该是 `owner` |
| 4 | `.keys()` 多余 | `if owner not in cell_dict` 就够了,dict 的 `in` 默认查 key |

**Python 引用机制(这道题的核心知识点):**
```python
# 错误: 一个 list, 多个 key 指向它
a = []
d = {"x": a, "y": a}
a.append(1)
print(d)   # {"x": [1], "y": [1]}  ← 都变了!

# 正确: 每个 key 各自的 list
d = {"x": [], "y": []}
d["x"].append(1)
print(d)   # {"x": [1], "y": []}   ← 互不影响
```

**正确写法:**
```python
# 方法 1: 手动判断
cell_dict = {}
for cell, owner in cells_info:
    if owner not in cell_dict:
        cell_dict[owner] = []      # 每个 owner 创建独立的新 list
    cell_dict[owner].append(cell)

# 方法 2: setdefault 一行搞定
cell_dict = {}
for cell, owner in cells_info:
    cell_dict.setdefault(owner, []).append(cell)
```

**核心教训:** Python 变量存的是引用(像指针)。`d[k] = some_list` 不是复制 list,是让 key 指向同一个 list。要让每个 key 有独立的 list,必须每次 `= []` 创建新的。

---

### 练习 5(e): 分隔线硬编码宽度

**原始写法:**
```python
print("-" * 15 + "+" + "-" * 15 + "+" + ...)   # 手动拼,改宽度就得重算
```

**更好的写法:**
```python
header = f"{'Corner':<10} | {'vth':>6} | ..."
print(header)
print("-" * len(header))   # 用 len() 自动算宽度
```

---

## 二、语法知识点

### 1. f-string 里能放什么

`{}` 里能放任何**表达式**(expression),不能放**语句**(statement):

```python
# 能放
f"{w / l:.1f}"                            # 算术
f"{max(vth_list)}"                        # 函数调用
f"{'PASS' if gain >= 40 else 'FAIL'}"     # 三元表达式
f"{[c for c in corners if t > 0]}"        # 列表推导式
f"{w=}"                                   # debug 格式(3.8+),打印 w=1.2e-06

# 不能放
f"{x = 5}"          # 赋值语句
f"{for x in xs}"    # 循环语句
```

**引号嵌套规则(3.12 以下):** 外层双引号,内层必须用单引号:
```python
f"{d['key']}"    # ✅
f"{d["key"]}"    # ❌ 3.12 以下报错
```

### 2. 生成器表达式 vs 列表推导式

```python
[x*2 for x in range(5)]     # 列表推导式 → [0, 2, 4, 6, 8],立刻全部算完存内存
(x*2 for x in range(5))     # 生成器表达式 → 惰性求值,遍历时才算,只能用一次
```

| | 列表推导式 `[...]` | 生成器表达式 `(...)` |
|---|---|---|
| 返回类型 | list | generator |
| 内存 | 全部存内存 | 几乎不占 |
| 能否下标/len | 可以 | 不行 |
| 能否多次遍历 | 可以 | 只能一次 |
| 适合 | 需要保留结果 | 一次性喂给 sum/max/any/all |

当生成器表达式是函数**唯一参数**时,可以省掉外层括号:
```python
sum((x*x for x in range(10)))   # 完整写法
sum(x*x for x in range(10))     # 省略写法,等价
```

### 3. any() / all()

```python
any(iterable)   # 有一个为真 → True;  全假 → False   (相当于 or)
all(iterable)   # 全部为真 → True;    有一个假 → False (相当于 and)
```

配合生成器表达式使用,而且**短路求值**——`any` 遇到第一个 True 立刻停,`all` 遇到第一个 False 立刻停:

```python
# 所有 corner 的 gain 都 ≥ 40?
all(r["gain"] >= 40 for r in results.values())

# 有没有任何 corner 的 pm < 60?
any(r["pm"] < 60 for r in results.values())
```

### 4. 解包 (Unpacking)

```python
# 基本解包
name, temp, vdd = ("tt_25c", 25, 1.2)

# for 循环自动解包
for cell, owner in cells_info:           # 拆 (cell, owner)
for corner, params in pvt_table.items(): # 拆 (key, value)

# * 收集剩余
first, *rest = [1, 2, 3, 4]             # first=1, rest=[2, 3, 4]
*_, cell, view = path.split("/")         # 只要最后两段

# ** 字典解包
all_results = {**josn_results, **mike_results}   # 合并字典
run_sim(**sim_config)                             # 解包成关键字参数

# 交换
a, b = b, a
```

### 5. sorted() 对 dict 排序

dict 本身没有排序方法,用 `sorted()` 排完重新构建:

```python
d = {"ss": 38.21, "tt": 45.67, "ff": 52.04}

# 按 value 升序,得到排好序的 (key, value) 对
sorted(d.items(), key=lambda kv: kv[1])

# 按 value 降序
sorted(d.items(), key=lambda kv: kv[1], reverse=True)

# 结果要 dict → 外面套 dict()
d_sorted = dict(sorted(d.items(), key=lambda kv: kv[1]))
```

### 6. 方法调用 vs 方法对象(加不加括号)

```python
d.items()     # 加括号 → 调用方法,拿到 dict_items 对象(可迭代)
d.items       # 不加   → 方法对象本身(一个函数)

# 需要"调用结果"的场景:
sorted(d.items())              # ✅ sorted 需要可迭代对象
len(d.keys())                  # ✅ len 需要有长度的对象

# 需要"函数本身"的场景:
sorted(d, key=d.get)           # ✅ key= 需要一个函数,sorted 内部帮你调用
max(pvt_table, key=get_vth)    # ✅ 传函数本身,不是调用结果
```

### 7. max() 的 key 参数

`key=` 接受任何**可调用对象**(callable),不限于 lambda:

```python
# lambda(匿名函数)
max(d.items(), key=lambda kv: kv[1]["vth"])

# 普通 def 函数
def get_vth(kv):
    return kv[1]["vth"]
max(d.items(), key=get_vth)     # 注意不加括号

# 内置函数
max(["ldo", "bandgap", "pll"], key=len)

# 方法本身
max(simple_dict, key=simple_dict.get)
```

### 8. f-string 宽度对齐

```python
f"{'Corner':<10}"     # 左对齐,总宽 10   → "Corner    "
f"{'Corner':>10}"     # 右对齐             → "    Corner"
f"{'Corner':^10}"     # 居中               → "  Corner  "
f"{'Corner':*<10}"    # 左对齐,用 * 填充  → "Corner****"
f"{0.45:>8.3f}"       # 右对齐,宽 8,3 位小数 → "   0.450"
f"{1.05e5:>10.2e}"    # 科学计数           → "  1.05e+05"
```

宽度是**最小宽度**,内容超过不会截断。
