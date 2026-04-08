#!/bin/bash
# 把当前 Claude 的最新记忆文件同步回仓库（提交前用）
# 用法: bash sync-memory.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
MEMORY_SRC="$HOME/.claude/projects/-home-josn/memory"
MEMORY_DST="$REPO_DIR/claude-memory"

if [ ! -d "$MEMORY_SRC" ]; then
    echo "错误: 找不到 $MEMORY_SRC"
    exit 1
fi

mkdir -p "$MEMORY_DST"
cp "$MEMORY_SRC"/*.md "$MEMORY_DST/"
echo "已同步记忆文件到仓库:"
ls "$MEMORY_DST"
