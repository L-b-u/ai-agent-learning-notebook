"""
🎯 任务一（基础关，约 20 分钟）：定义"宠物"类

要求：

1. 定义一个 `Pet` 类，有属性：`name`（名字）、`species`（种类，如"猫""狗"）、`energy`（精力值，初始 100）。
2. 有方法 `play()`：玩一次精力值减 20，打印"XX玩得很开心，剩余精力XX"。如果精力已经为 0，打印"XX累坏了，玩不动了"。
3. 有方法 `eat()`：吃一次精力值加 30（上限 100），打印"XX吃饱了，精力恢复到XX"。
4. 创建两个宠物对象，分别玩几次、吃几次，观察精力值变化。

"""


class Pet:
    def __init__(self, name, species, energy):
        self.name = name
        self.species = species
        self.energy = energy

    def play(self):
        self.energy -= 20
        if self.energy <= 0:
            print(f"{self.name}累坏了，玩不动了")
        else:
            print(f"{self.name}玩得很开心,剩余精力{self.energy}")

    def eat(self):
        self.energy += 30
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name}吃饱了，精力恢复到{self.energy}")


cat = Pet("小花", "猫", 100)
cat.play()
cat.eat()
dog = Pet("旺财", "狗", 100)
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.eat()
