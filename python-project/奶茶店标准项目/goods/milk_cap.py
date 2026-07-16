# goods/milk_cap.py - 奶盖茶子类
# 继承BaseDrink，实现奶盖茶专属优惠：购买2杯及以上立减3元
# 实例属性，__milk_cap_cost
# get_milk_cap_cost()   -->获取奶盖的单杯价格

#测试代码

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from goods.base_drink import BaseDrink


class MilkCapTea(BaseDrink):
    def __init__(self, name: str, price: float,):
        super().__init__(name, price)
        self.__milk_cap_cost = 6
    def get_final_price(self, buy_num: int) -> float:
        origin = self.price * buy_num
        if buy_num >= 2:
            final = origin * self.shop_discount - 3
        else:
            final = origin * self.shop_discount
        print("=====")
        return round(final, 2)

    def get_milk_cap_cost(self) -> float:
        return self.__milk_cap_cost

if __name__ == "__main__":
    milk_cap = MilkCapTea("奶盖",20 )
    BaseDrink.set_shop_discount(0.9)
    print(f"购买一杯奶盖的价格为:{milk_cap.get_final_price(1)}")
    print(f"购买两杯奶盖的价格为:{milk_cap.get_final_price(2)}")
    print(f"奶盖的成本为:{milk_cap.get_milk_cap_cost()}")
