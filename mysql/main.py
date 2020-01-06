

class Hero:

    # 初始化英雄参数
    def __init__(self,name,type,hp,mp,def_,attack):

        self.name = name
        self.type = type
        self.hp = hp
        self.mp = mp
        self.def_ = def_
        self.attack = attack
        self.exp = 0
        self.level = 1

    def __str__(self):
        return (("欢迎来到，KK联盟。英雄名称：%s,英雄类型：%s,生命值：%s,魔法值：%s,"
                 "防御力：%s,攻击力：%s,当前等级：%s,升级所需经验:%s"
                 ) % (self.name,self.type,self.hp,
                   self.mp,self.def_,self.attack,self.level,500-self.exp))

    def hunting(self):
        self.exp += 100
        print("你得到100经验值")
        if self.exp == 500:
            self.level += 1
            self.hp += 50
            self.mp += 20
            self.def_ += 10
            self.attack += 15
            print("恭喜你升级到%s级" % self.level)
            self.exp = 0

kimi = Hero("kimi","法师",500,200,50,30)
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)
kimi.hunting()
print(kimi)

