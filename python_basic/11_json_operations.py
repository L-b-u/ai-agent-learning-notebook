# 11_json_operations.py — JSON 序列化与反序列化

import json
import os
import tempfile

temp_dir = tempfile.gettempdir()
json_file = os.path.join(temp_dir, "demo_data.json")

# 1. Python 对象 → JSON 字符串 (json.dumps)
data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True,
    "score": None
}
json_str = json.dumps(data, ensure_ascii=False, indent=4)
print(f"  dumps 结果：\n{json_str}")

# 常用参数说明
print("\n  参数说明：")
print("    ensure_ascii=False  — 允许中文字符直接输出")
print("    indent=4            — 格式化缩进")
print("    sort_keys=True      — 按键排序输出")

# 2. JSON 字符串 → Python 对象 (json.loads)
print("\n--- 2. 反序列化：JSON → Python ---")
json_input = '{"name": "李四", "age": 30, "city": "北京"}'
obj = json.loads(json_input)
print(f"  loads 结果：{obj}")
print(f"  类型：{type(obj).__name__}")

# 类型映射表
print("\n  JSON ↔ Python 类型映射：")
print("    JSON object  ↔ dict")
print("    JSON array   ↔ list")
print("    JSON string  ↔ str")
print("    JSON number  ↔ int / float")
print("    JSON true    ↔ True")
print("    JSON false   ↔ False")
print("    JSON null    ↔ None")

# 3. 写入 JSON 文件 (json.dump)
print("\n--- 3. dump 写入文件 ---")
users = [
    {"id": 1, "name": "张三", "score": 95},
    {"id": 2, "name": "李四", "score": 88},
    {"id": 3, "name": "王五", "score": 76},
]
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
print(f"  已写入：{json_file}")

# 4. 读取 JSON 文件 (json.load)
print("\n--- 4. load 读取文件 ---")
with open(json_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"  读取结果：{loaded}")
print(f"  共 {len(loaded)} 条记录")

# 5. 自定义 JSON 编码器（处理 datetime 等特殊类型）
print("\n--- 5. 自定义序列化 ---")
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

complex_data = {
    "task": "数据分析",
    "timestamp": datetime.now(),
    "count": 42
}
result = json.dumps(complex_data, cls=CustomEncoder, ensure_ascii=False)
print(f"  含 datetime 的 JSON：{result}")

# 6. 清理临时文件
os.remove(json_file)

