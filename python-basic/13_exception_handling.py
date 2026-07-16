# 13_exception_handling.py — 异常处理 try / except / finally / raise

# 1. 基本 try / except

def safe_divide(a, b):
    try:
        result = a / b
        print(f"  {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print(f"  错误：不能除以零")
        return None

safe_divide(10, 2)
safe_divide(10, 0)

# 2. 捕获多种异常
print("\n--- 2. 多种异常捕获 ---")

def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"  ValueError：'{value}' 不是有效数字")
    except TypeError:
        print(f"  TypeError：'{value}' 类型不支持转换")
    except Exception as e:
        print(f"  未预期异常：{type(e).__name__}: {e}")

safe_int_convert("42")
safe_int_convert("abc")
safe_int_convert(None)

# 3. try / except / else / finally
print("\n--- 3. try/except/else/finally ---")

def read_file_safe(path):
    try:
        f = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"  文件不存在：{path}")
    else:
        # 仅在无异常时执行
        content = f.read()
        f.close()
        print(f"  读取成功，内容：{content.strip()}")
    finally:
        # 无论是否异常都执行（适合清理资源）
        print("  [finally] 清理完成")

read_file_safe("nonexistent_file.txt")

# 4. raise 抛出异常
print("\n--- 4. raise 主动抛出异常 ---")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"年龄必须是整数，但传入了 {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"年龄 {age} 不在合理范围 0-150")
    return age

# 正常调用
print(f"  年龄 25：{validate_age(25)}")

# 异常调用
try:
    validate_age(-5)
except ValueError as e:
    print(f"  捕获到：{e}")

# 5. 自定义异常类
print("\n--- 5. 自定义异常类 ---")

class ConfigError(Exception):
    """配置相关异常"""
    def __init__(self, key, message="配置缺失"):
        self.key = key
        self.message = f"{message}：{key}"
        super().__init__(self.message)

def load_config(key):
    config = {"host": "localhost", "port": 8080}
    if key not in config:
        raise ConfigError(key)
    return config[key]

try:
    load_config("database")
except ConfigError as e:
    print(f"  {e}")

# 6. 异常处理最佳实践
print("\n--- 6. 最佳实践 ---")
print("  1️⃣ 捕获具体异常，避免裸 except Exception")
print("  2️⃣ 不要在 except 块中沉默吞掉异常（至少打日志）")
print("  3️⃣ finally 用于资源清理（关闭文件、释放锁等）")
print("  4️⃣ 自定义异常让错误信息更有语义")
print("  5️⃣ 异常信息包含上下文细节以方便排查")

