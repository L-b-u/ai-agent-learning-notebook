# 继承BaseDrink，实现果茶专属优惠：全场折扣基础上额外95折

#重写打印小票方法：显示果茶专属优惠信息

#测试代码

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from goods.base_drink import BaseDrink


class FruitTea(BaseDrink):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        self.type = "果茶"

    def get_final_price(self, buy_num: int) -> float:
        origin = self.price * buy_num
        final = origin * self.shop_discount * 0.95
        print("=====")
        return round(final, 2)


if __name__ == "__main__":
    fruit_tea = FruitTea("果茶", 15)
    BaseDrink.set_shop_discount(0.9)
    print(f"一杯水果茶的价格为:{fruit_tea.get_final_price(1)}")
    print(f"两杯水果茶的价格为:{fruit_tea.get_final_price(2)}")