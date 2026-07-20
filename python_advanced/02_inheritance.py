# 02_inheritance.py — 继承、重写、多态、super()

# 1. 基本继承与方法重写

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} 发出了声音"

    def info(self):
        return f"物种: {self.species}, 名字: {self.name}"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 喵喵!"

    def purr(self):
        return f"{self.name} 在打呼噜"

cat = Cat("小咪", "猫")
print(f"  {cat.info()}")
print(f"  {cat.speak()}")
print(f"  {cat.purr()}")

# 2. super() 调用父类方法

class Pet(Animal):
    def __init__(self, name, species, owner):
        super().__init__(name, species)
        self.owner = owner

    def info(self):
        return f"{super().info()}, 主人: {self.owner}"

class Dog(Pet):
    def __init__(self, name, owner, job):
        super().__init__(name, "狗", owner)
        self.job = job

    def speak(self):
        return f"{self.name}: 汪汪! 正在执行任务「{self.job}」"

pet = Pet("旺财", "狗", "小明")
print(f"\n  {pet.info()}")
dog = Dog("闪电", "警察局", "缉毒")
print(f"  {dog.info()}")
print(f"  {dog.speak()}")

# 3. 多态：同一接口，不同行为

class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("子类必须实现 pay 方法")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"信用卡支付 {amount} 元"

class WeChatPay(PaymentMethod):
    def pay(self, amount):
        return f"微信支付 {amount} 元"

def checkout(method, amount):
    return method.pay(amount)

for m in [CreditCard(), WeChatPay()]:
    print(f"  {checkout(m, 100)}")

# 4. isinstance / issubclass / MRO

print(f"\n  cat 是 Cat 实例? {isinstance(cat, Cat)}")
print(f"  cat 是 Animal 实例? {isinstance(cat, Animal)}")
print(f"  Cat 是 Animal 子类? {issubclass(Cat, Animal)}")
print(f"  Dog MRO: {[c.__name__ for c in Dog.__mro__]}")
