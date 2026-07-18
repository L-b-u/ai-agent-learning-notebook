"""
🎯 任务二（进阶关，约 25 分钟）：用继承做"工作犬"

要求：

1. 让 `WorkingDog` 继承 `Pet`，新增属性 `job`（工作类型，如"导盲""搜救"）。
2. 新增方法 `work()`：工作一次精力减 40，打印"XX（工作类型）执行任务，剩余精力XX"。精力不足 40 时打印"XX精力不足，无法执行任务"。
3. 重写 `play()`：工作犬玩的时候打印"XX虽然是工作犬，但也要放松一下"，精力照常减 20。
4. 创建一个工作犬对象，演示它工作、玩、吃饭的过程。
"""


class WorkingDog(Pet):
    def __init__(self, name, species, energy, job):
        super().__init__(name, species, energy)
        self.job = job

    def work(self):
        self.energy -= 40
        if self.energy >= 40:
            print(f"{self.name}正在执行{self.job}任务,剩余精力{self.energy}")
        else:
            print(f"{self.name}精力不足，无法执行任务,剩余精力{self.energy}")

    def play(self):
        self.energy -= 20
        print(f"工作犬玩的时候打印{self.name}虽然是工作犬，但也要放松一下,剩余精力{self.energy}")


work_dog = WorkingDog("豆豆", "狗", 100, "导盲")
work_dog.work()
work_dog.play()
work_dog.work()
work_dog.eat()