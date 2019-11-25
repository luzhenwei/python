#根据杀敌个数
# 输出不同提示音
class KillEnemy(object):
    def print_0(self):
        print("杀敌0个，猥琐发育")
    def print_s(self,num):
        if num >= 3:
            print("已经暴走！！！")
        else:
            print("猥琐发育别浪！！！")

killEnemy = KillEnemy()
killEnemy.print_s(3)