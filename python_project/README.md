---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 32fb7564cc05ce0a9bbe082b6a63528a_62c1bede80f211f188d5525400bff409
    ReservedCode1: C1defoFslLdniygrB405HdvFv9hvUlzVekxWXymNGtmKdUeIGpQvWYIKso/OyiPibHPrxUFBHOblsVlPII5R5fUSCtBMTywdatD1XhMRewvrjvj595T8iaaf7FjjF+oRUPkkT7uxUOmJtYlHJWkGapaIKqqErT2KMXM/hCrUp+/6bUhJ657FRsgP2zA=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 32fb7564cc05ce0a9bbe082b6a63528a_62c1bede80f211f188d5525400bff409
    ReservedCode2: C1defoFslLdniygrB405HdvFv9hvUlzVekxWXymNGtmKdUeIGpQvWYIKso/OyiPibHPrxUFBHOblsVlPII5R5fUSCtBMTywdatD1XhMRewvrjvj595T8iaaf7FjjF+oRUPkkT7uxUOmJtYlHJWkGapaIKqqErT2KMXM/hCrUp+/6bUhJ657FRsgP2zA=
---

# python_project — 项目总览

> Python 综合实践项目集合，涵盖 OOP、多线程并发、装饰器、生成器、JSON 持久化等核心技术。

---

## 项目列表

| 项目 | 目录 | 核心技术 |
|------|------|---------|
| 魔法技能加点器 | [`魔法技能加点器/`](<魔法技能加点器/>) | 装饰器、生成器、lambda、异常处理、JSON 持久化 |
| AI 推理调度系统 | [`ai_scheduler/`](<ai_scheduler/>) | 多线程并发、GIL 分析、策略模式、OOP 多态、Lock 线程安全 |

---

## 快速开始

### 魔法技能加点器
```bash
cd "D:\ai-agent-study\python-project\魔法技能加点器"
python 项目.py
```
交互式 RPG 角色加点系统，输入数值加点，退出时自动保存。另含 `18_comprehensive_project.py`（从 python-basic 移入），为同一项目的装饰器/生成器整合版本。详见 [魔法技能加点器.md](<魔法技能加点器/魔法技能加点器.md>)。

### AI 推理调度系统
```bash
cd "D:\ai-agent-study\python-project\AI推理任务指挥官"
python ai_scheduler.py
```
多用户 AI 推理任务调度，对比串行 vs 并发性能。预期加速比约 4x。另含 `08_comprehensive_project.py`（从 python_advanced 移入），为同一项目的 OOP+多线程整合版本。详见 [ai_scheduler.md](<AI推理任务指挥官/ai_scheduler.md>)。

---

## 目录结构

```
python_project/
├── README.md                    # 本文件（总览）
├── 魔法技能加点器/               # 项目一
│   ├── 项目.py
│   ├── 18_comprehensive_project.py  # 从 python-basic 移入
│   ├── role_json.json
│   ├── role_save.txt
│   └── 魔法技能加点器.md
└── AI推理任务指挥官/              # 项目二
    ├── ai_scheduler.py
    ├── 08_comprehensive_project.py  # 从 python_advanced 移入
    ├── test.py
    ├── 思考题.txt
    ├── report.txt
    └── ai_scheduler.md
```

---

## 技术图谱

| 技术 | 魔法技能加点器 | AI 调度系统 |
|------|:---:|:---:|
| OOP 继承多态 | - | ✅ |
| 多线程 + Lock | - | ✅ |
| datetime 计时 | - | ✅ |
| 装饰器 | ✅ | - |
| 生成器 yield | ✅ | - |
| 列表推导式 | ✅ | - |
| JSON 持久化 | ✅ | - |
| 异常处理 | ✅ | - |
| NotImplementedError | - | ✅ |
| 性能对比报表 | - | ✅ |

---

## 学习路径建议

1. **魔法技能加点器** → 理解装饰器、生成器、异常处理等 Python 基础进阶特性
2. **AI 推理调度系统** → 理解 OOP 多态、多线程并发、GIL 机制等系统设计能力
3. 阅读各项目的 `.md` 文档进行深度复习
*（内容由AI生成，仅供参考）*
*（内容由AI生成，仅供参考）*
