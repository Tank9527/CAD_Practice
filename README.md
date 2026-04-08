# Python 练习仓库

CAD 工程师的 Python 学习练习，包含 Claude 的记忆文件备份，方便跨设备使用。

## 目录结构

- `day01/`, `day02/`, ... — 按天组织的练习代码
- `claude-memory/` — Claude Code 自动记忆文件备份
- `setup-new-machine.sh` — 新机器上克隆后恢复记忆的脚本
- `sync-memory.sh` — 把本机最新记忆同步回仓库

## 在新机器上使用

```bash
# 1. 克隆仓库
git clone <你的仓库地址> ~/python-practice
cd ~/python-practice

# 2. 恢复 Claude 记忆
bash setup-new-machine.sh

# 3. 启动 Claude Code，新机器就能"认出"你了
```

## 日常使用流程

每次练习完想推到 GitHub 时：

```bash
cd ~/python-practice

# 把当前 Claude 的最新记忆同步回仓库
bash sync-memory.sh

# 提交代码和记忆
git add .
git commit -m "day02 dict 进阶练习"
git push
```
