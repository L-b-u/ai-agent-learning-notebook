"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
# a 与 y,z 比 c 与 y比 所以a和z比 b和x比
list_1 = ['x', 'y', 'z']
for a in list_1:
    for b in list_1:
        for c in list_1:
            if a != b and a != c and b != c and a != list_1[0] and c != list_1[0] and c != list_1[2]:
                print(f"a:{a} b:{b} c:{c}")