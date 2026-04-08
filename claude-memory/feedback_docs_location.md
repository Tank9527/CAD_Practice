---
name: docs-save-location
description: All generated documents should be saved to /mnt/d/AI/doc by default, with category subfolders
type: feedback
---

所有生成的文档默认保存到 `/mnt/d/AI/doc` 目录下，按类别分子目录存放（例如 `/mnt/d/AI/doc/python/`、`/mnt/d/AI/doc/eda/`）。

其他类别的资料仍可放在 `/mnt/d/AI/` 下的同级目录（例如 `/mnt/d/AI/python-learning`、`/mnt/d/AI/Claude使用指南`），但**新生成的文档**默认进 `doc/`。

**Why:** 用户在 2026-04-03 明确指定 `/mnt/d/AI/doc` 作为写文档的统一输出路径，方便集中管理。位于 Windows D 盘。
**How to apply:** 每次生成文档（笔记、说明、报告等）时，写入 `/mnt/d/AI/doc/<类别>/`，不要存到 `~/doc`、当前工作目录或 `/mnt/d/AI/` 根目录下。如果不确定类别，先问用户。
