# Git 使用方法

> 本文档记录从零开始使用 Git 管理项目并推送至 GitHub 的完整流程。

---

## 1. 初始化本地仓库

```bash
git init
```

**解析：**
在当前目录下创建一个隐藏的 `.git` 文件夹，将其初始化为 Git 仓库。之后 Git 才会开始追踪该目录下的文件变更。

---

## 2. 将文件添加到暂存区

```bash
git add README.md
```

**解析：**

| 参数 | 说明 |
|------|------|
| `README.md` | 要添加的文件名，这里指定只添加 `README.md` |

把 `README.md` 的当前快照放入暂存区（staging area），告诉 Git"我准备提交这个文件的这次修改"。如果想添加当前目录所有文件，可将 `README.md` 替换为 `.`：

```bash
git add .
```

---

## 3. 提交到本地仓库

```bash
git commit -m "first commit"
```

**解析：**

| 参数 | 说明 |
|------|------|
| `-m` | 表示后面紧跟提交信息（message） |
| `"first commit"` | 本次提交的说明文字，用于标记这次提交做了什么 |

将暂存区的内容正式保存到本地仓库的历史记录中，`"first commit"` 可以改成任何你想要的描述，如 `"初始化项目结构"`。

---

## 4. 修改默认分支名称

```bash
git branch -M main
```

**解析：**

| 参数 | 说明 |
|------|------|
| `-M` | 强制重命名分支（move/rename），即使目标分支名已存在也会覆盖 |
| `main` | 新的分支名称，这里把默认的 `master` 改成 `main` |

Git 2.28 之前默认分支叫 `master`，现在社区普遍使用 `main`。这步就是把本地分支重命名为 `main`。如果你的 Git 版本默认已经创建的是 `main`，这步可跳过。

---

## 5. 关联远程仓库

```bash
git remote add origin https://github.com/L-b-u/ai-agent-learning-notebook.git
```

**解析：**

| 参数 | 说明 |
|------|------|
| `remote add` | 添加一个远程仓库的引用 |
| `origin` | 给这个远程仓库起的别名，约定俗成叫 `origin`（可以改成其他名字） |
| `https://github.com/...` | 远程仓库的 URL 地址，这里是你的 GitHub 仓库链接 |

这步告诉本地 Git："以后提到 `origin`，就是指 `https://github.com/L-b-u/ai-agent-learning-notebook.git` 这个远程仓库"。关联成功后，才能执行推送操作。

---

## 6. 推送到远程仓库

```bash
git push -u origin main
```

**解析：**

| 参数 | 说明 |
|------|------|
| `push` | 将本地提交推送到远程仓库 |
| `-u` | 设置上游（upstream）分支，之后只需 `git push` 即可，不用再写 `origin main` |
| `origin` | 目标远程仓库别名，对应第 5 步关联的地址 |
| `main` | 要推送的本地分支名 |

将本地 `main` 分支的所有提交上传到 GitHub 仓库。`-u` 会让 Git 记住这个对应关系，以后在该分支直接 `git push` 就行。

---

## 完整流程速览

| 步骤 | 命令 | 作用 |
|------|------|------|
| ① | `git init` | 初始化本地仓库 |
| ② | `git add README.md` | 将指定文件加入暂存区 |
| ③ | `git commit -m "first commit"` | 提交到本地仓库 |
| ④ | `git branch -M main` | 重命名默认分支为 main |
| ⑤ | `git remote add origin <仓库地址>` | 关联远程 GitHub 仓库 |
| ⑥ | `git push -u origin main` | 推送代码到远程仓库 |

---

## 日常更新流程

完成首次推送后，后续每次修改代码只需三步：

### 1. 加入暂存区

```bash
git add 你的文件名.py
```

**解析：**

| 参数 | 说明 |
|------|------|
| `你的文件名.py` | 替换为你要提交的文件名，如 `main.py`、`utils.py` |

也可以一次性添加所有修改过的文件：

```bash
git add .
```

### 2. 提交并写备注

```bash
git commit -m "描述本次更新内容"
```

**解析：**

| 参数 | 说明 |
|------|------|
| `-m` | 后跟提交信息（message） |
| `"描述本次更新内容"` | 替换为本次改了什么，如 `"修复登录页面样式错乱"`、`"新增用户导出功能"` |

### 3. 推送到 GitHub

```bash
git push
```

**解析：**

由于首次推送时已用 `-u` 绑定了上游分支，后续直接 `git push` 即可，无需再写 `origin main`。

---

## 完整流程速览（更新版）

| 场景 | 步骤 | 命令 |
|------|------|------|
| 首次搭建 | ①~⑥ | 见上方完整流程 |
| 日常更新 | ① | `git add 文件名.py` |
|  | ② | `git commit -m "描述"` |
|  | ③ | `git push` |


