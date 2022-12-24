import random
import time


class Forest:
    def __init__(self, count: int, *monster):
        forest_count = []
        for i in range(count):
            forest_count.append(random.choice(monster))
        self.forest_count = forest_count
        self.monster = monster

dd = 1
cc = 1
ShuaGuaiLu = random.randint(1, 10)

class wolf:
    monster_name = '狼妖'


class bird:
    monster_name = '鹰妖'


class Soldier:
    def __init__(self, strength):
        self.strength = strength
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'


def Kong():
    print("\n\n")


def ChaKanZhuangBei():
    time.sleep(0.5)
    print("\n装备栏: ", ZhuangBeiLan)
    ShiQing()

def ChaKanWuPin():
    time.sleep(0.5)
    print("\n物品栏: ", WuPinLan)
    ShiQing()

class Aman(Soldier):
    WuPinLan = []
    FuJia = 5
    HuJia = 5
    SuDu = 5
    ZhuangBeiLan = []
    XueLiang = 100
    HuJiaFuJia = 0

    def __init__(self):
    self.soldier_hp_now = 100

    # 定义治疗方法，血满则不加，其他时候加，加了发现比最大血量多了，就设置为最大血量
    if self.soldier_hp_now == self.soldier_hp_max:
        print(‘不能加血’)
    else:
        if self.soldier_hp_now > self.soldier_hp_max:
            self.soldier_hp_now = self.soldier_hp_max
        print(self.soldier_hp_now)




    def fight(self, enemy_name):
        if enemy_name == self.enemy_god:
            self.soldier_hp_now -= 20
        elif enemy_name == self.enemy_bad:
            self.soldier_hp_now -= 80
        else:
            print('血量不变')



class Axe(Soldier):
    soldier_type = '斧头兵'
    soldier_price = 120
    soldier_hp_max = 120
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'

    def __init__(self, soldier_name):
        self.soldier_hp_now = 120
        self.soldier_name = soldier_name


# 弓箭类
class Arch(Soldier):
    soldier_name = '弓箭兵'
    soldier_price = 100
    soldier_hp_max = 100
    enemy_god = '狼妖'
    enemy_bad = '鹰妖'

    def __init__(self, soldier_name):
        self.soldier_hp_now = 100
        self.soldier_name = soldier_name

ef ShiQing():
    print("\n现在你要:")
    print("1.出发  2.装备  3.查看装备\n4.查看物品  5.查看状态  6.吃东西")
    v = int(input(">> "))
    if v == 1:
        ChuFa()
    elif v == 2:
        ZhuangBei()
    elif v == 3:
        ChaKanZhuangBei()
    elif v == 4:
        ChaKanWuPin()
    elif v == 5:
        ShuXing()
    elif v == 6:
        ShiYong()
    else:
        print("请重新输入!")


class Player:
    def __init__(self):
        self.money = 1000
        self.army = {}
    def hire(self, soldier):
        banlance = self.money - soldier.soldier_price
        if soldier.soldier_name in self.army:
            print('取名重复，请重新取名')
        elif banlance >= 0:
            self.money -= soldier.soldier_price
            self.army[soldier.soldier_name] = soldier
            print(f'雇佣小兵成功{self.money}')
        else:
            print('雇佣小兵失败')


print('========开始游戏=======\n')
print("你好!")
print("欢迎来玩这个游戏"
forest_list = Forest(7, wolf, hawk)
print(f'七个关卡的怪物分别是\n')
for i in forest_list.forest_count:
    print(i.monster_name)
print('10秒钟后文字消失\n')
time.sleep(10)
for i in range(10):
    print('\n')


class GuaiWu:
    def XiaoGuai(self):
        global XiaoGuaiXie, XiaoGuaiGongJi, GuaiSu
        XiaoGuaiXie = random.randint(15, 30)
        XiaoGuaiGongJi = random.randint(5, 15)
        GuaiSu = 8
        print('妖')
        time.sleep(0.5)
        print('小兵' % (XiaoGuaiXie, XiaoGuaiGongJi, GuaiSu))




player1 = Player()
print(f'===========你有{player1.money}元,===========')
while True:
    fighter_type = input('需要雇佣哪种小兵\n---1.斧头兵 2.弓箭兵---\n'
                         '---输入6可查看已经雇佣的小兵---\n---输入5退出雇佣环节--\n')
    if fighter_type.isdigit():
        fighter_type = int(fighter_type)
        if fighter_type == 1:
            name = input('---请随便入给你的斧头兵取个名字吧---\n')
            player1.hire(Axe(name))
        elif fighter_type == 2:
            name = input('---请随便入给你的弓箭兵取个名字吧---\n')
            player1.hire(Arch(name))
        elif fighter_type == 3:
            print(f'你当前余额{player1.money}')
        elif fighter_type == 6:
            for i in player1.army.keys():
                print(i)
        elif fighter_type == 5:
            break
        else:
            print('---输入错误\n---')
    else:
        print(f'---{type(fighter_type)}请重新输入\n')





print(f'=====================开始======================\n')
game_end = 1
for i in range(len(forest_list.forest_count)):
    if game_end == 0:
        break
    print(f'--------------------欢迎来到第{i + 1}关---------------------\n')
    while True:
        if len(player1.army) == 0:
            print('士兵阵亡，失败\n')
            game_end = 0
            break
        else:
            fighter = input(f'--请选择出征士兵，输入（army）查看--\n')
            if fighter == 'army':
                for k in player1.army.keys():
                    print(k)
            else:
                if fighter in player1.army:
                    player1.army[fighter].fight(not forest_list.forest_count[i].monstr_name)
                    fighter_hp=player1.army[fighter].soldier_hp_now
                    print(fighter_hp)
                    if fighter_type > 0:
                        while True:
                            treat_count = input(f'---成功，继续闯关，输入{fighter}可查看血量---\n')
                            if treat_count.isdigit():
                                if player1.money > int(treat_count):

                                    player1.army[fighter].treat(int(treat_count))
                                    break
                            else:
                                print('money不足')
                    else:
                            print('---错误输入---\n')
                    break
                elif fighter_hp < 0:
                    del player1.army[fighter]
                    print(f'---{fighter}战斗后剩余血量{fighter_hp}，失败，---\n')
                    continue
                else:
                    print('输入名称错误\n')

if game_end == 1:
    print(f'剩余money数{player1.money}')
elif game_end == 0:

    print('游戏结束')