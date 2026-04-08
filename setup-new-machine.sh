#!/bin/bash
# 在新机器上克隆这个仓库后，运行这个脚本来恢复 Claude 的记忆文件
# 用法: bash setup-new-machine.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
MEMORY_SRC="$REPO_DIR/claude-memory"
MEMORY_DST="$HOME/.claude/projects/-home-josn/memory"

echo "=== Claude 记忆恢复脚本 ==="
echo "源目录: $MEMORY_SRC"
echo "目标目录: $MEMORY_DST"
echo ""

if [ ! -d "$MEMORY_SRC" ]; then
    echo "错误: 找不到 $MEMORY_SRC"
    exit 1
fi

mkdir -p "$MEMORY_DST"

if [ -n "$(ls -A "$MEMORY_DST" 2>/dev/null)" ]; then
    echo "警告: 目标目录已有文件，将被覆盖"
    read -p "继续? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "已取消"
        exit 0
    fi
fi

cp "$MEMORY_SRC"/*.md "$MEMORY_DST/"
echo ""
echo "完成! 已恢复以下文件到 $MEMORY_DST :"
ls "$MEMORY_DST"
