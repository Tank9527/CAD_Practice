---
name: python-practice-repo
description: Location and cross-machine sync mechanism for the user's Python-for-CAD practice repo
type: project
---

用户的 Python 练习仓库在 `/home/josn/python-practice/`（git 仓库，有 `origin/main` 远端），按天组织目录：`day01/`、`day02/` …… 每天通常有若干 `NN_topic.py` + `NN_topic_extra.py` 的练习文件。学习 roadmap 在 `/mnt/d/AI/python-learning/learning-roadmap.md`（4 个阶段 30 天）。

仓库内带一套跨机器同步 Claude memory 的机制：
- `claude-memory/` —— memory 文件副本（随 git 一起走）
- `sync-memory.sh` —— 把 `~/.claude/projects/-home-josn/memory/*.md` 拷进 `claude-memory/`，提交前用
- `setup-new-machine.sh` —— 新机器克隆仓库后，反向把 `claude-memory/*.md` 恢复到 `~/.claude/projects/-home-josn/memory/`

**Why:** 用户在多台机器上继续同一套 Python 学习，需要 memory 跟着仓库走。仓库内的 `claude-memory/` 是副本而不是真源——真源永远是 `~/.claude/projects/-home-josn/memory/`。

**How to apply:**
- 用户说"继续学习""接着上次"时，练习文件去 `/home/josn/python-practice/dayNN/` 找，不要再去 `/mnt/d/AI/python-learning/`（那边只有 roadmap）。
- 如果在新机器上发现 memory 很空但仓库里的 `claude-memory/` 有内容，提醒用户跑 `setup-new-machine.sh`。
- 用户提到"同步 memory"或准备 commit 练习时，提醒先跑 `sync-memory.sh` 把 memory 副本更新进仓库。
- 不要直接编辑 `claude-memory/` 下的文件——那是同步产物，改了会被下次 `sync-memory.sh` 覆盖。
