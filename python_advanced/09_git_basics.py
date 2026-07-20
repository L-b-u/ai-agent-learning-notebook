# 07_git_basics.py — Git 基础命令参考

print("""
本文件为 Git 学习参考文档。在终端中执行以下命令（非 Python 代码）。

# 1. Git 配置（首次使用）

git config --global user.name "你的名字"
git config --global user.email "your@email.com"

# 2. 创建仓库

git init                    # 初始化当前目录为 Git 仓库
git clone <url>             # 克隆远程仓库到本地

# 3. 工作区 -> 暂存区 -> 仓库

git status                  # 查看文件状态
git add <file>              # 将文件加入暂存区
git add .                   # 将所有修改加入暂存区
git commit -m "提交信息"    # 提交暂存区到仓库
git log                     # 查看提交历史
git log --oneline           # 简洁版提交历史

# 4. 分支操作

git branch                  # 查看所有分支
git branch <name>           # 创建分支
git checkout <name>         # 切换分支
git checkout -b <name>      # 创建并切换分支
git merge <name>            # 合并分支到当前分支
git branch -d <name>        # 删除分支

# 5. 远程操作

git remote add origin <url>  # 添加远程仓库
git push origin <branch>     # 推送到远程
git pull origin <branch>     # 从远程拉取
git fetch                    # 获取远程更新（不合并）

# 6. 撤销与回退

git checkout -- <file>       # 撤销工作区修改
git reset HEAD <file>        # 撤销暂存区
git reset --soft HEAD~1      # 撤销最近一次 commit（保留修改）
git reset --hard HEAD~1      # 彻底撤销最近一次 commit
git revert <commit_id>       # 创建一个反向提交来回退

# 7. 最佳实践

# 1. 提交信息格式：type: 简短描述
#    如：feat: 添加用户登录功能  fix: 修复登录超时问题

# 2. 分支策略（Git Flow）：
#    main     - 生产环境
#    develop  - 开发主线
#    feature/*- 功能分支
#    hotfix/* - 紧急修复

# 3. .gitignore 文件：忽略不需要跟踪的文件
#    __pycache__/   .env    *.log    *.pyc

# 8. GitHub Quick Start

# echo "# my-project" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yourname/my-project.git
# git push -u origin main
""")

# Python 中操作 Git（使用 subprocess）
import subprocess
import os

def run_git_command(cmd, cwd="."):
    """安全的 Git 命令执行器"""
    try:
        result = subprocess.run(
            ["git"] + cmd.split(),
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"[Error] {result.stderr.strip()}"
    except FileNotFoundError:
        return "[Error] 未安装 Git 或不在 PATH 中"

# 示例：查看当前目录的 Git 状态（如果存在的话）
# print(run_git_command("status --short"))

