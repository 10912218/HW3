import random
print("恭喜你收到一隻簡大便")
print("你的每個行動都會影響他的未來")
health = random.randint(50,80)
strong = 0
happy = 30
fat = random.randint(50,80)
hunger = 50
Petlist=[health,strong,happy,fat,hunger]
day=[0]
def sleep():
    Petlist[0] +=3
    Petlist[3] -=2
    Petlist[4] -=3
def training():
    Petlist[0] +=1
    Petlist[1] +=3
    Petlist[2] -=4
    Petlist[3] -=1
    Petlist[4] -=4 
def exercise():
    Petlist[0] +=1
    Petlist[1] +=1
    Petlist[2] +=10
    Petlist[3] -=3
    Petlist[4] -=4
def feeding():
    Petlist[3] +=5
    Petlist[4] +=10
def play():
    Petlist[0] -=4
    Petlist[2] +=8
def Action():
    print("休息(A) 訓練(B) ㄉㄆ(C) 吃(D) 出去玩(E)")
    action=str(input("請選擇動作"))
    if action == "A":
        sleep()
        day[0]+=1
    elif action =="B":
        training()
        day[0]+=1
    elif action =="C":
        exercise()
        day[0]+=1
    elif action =="D":
        feeding()
        day[0]+=1
    elif action =="E":
        play()
        day[0]+=1
    else:
        print("未知動作，請重新輸入")
while 1:
    Action()
    print("大便數值:")
    print("健康度:",Petlist[0],"強壯度",Petlist[1],"親密度",Petlist[2],"肥胖度",Petlist[3],"飢餓度",Petlist[4])
    if Petlist[0] <= 0:
        print("你的大便不健康生病死了QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[1] >=100:
        print("恭喜養成一隻強壯簡大便!!")
        print("成就達成花了",day[0],"天")
        continue
    elif Petlist[2] <=0:
        print("你的寵物抑鬱症死了QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[2] >=100:
        print("恭喜養成一隻開心簡大便!!")
        print("成就達成花了",day[0],"天")
        print("恭喜變捲毛(打炮王)")
    elif Petlist[3] <=0:
        print("你的大便便皮包骨死了")
        print("生存天數",day[0],"天")
        break
    elif Petlist[3] >=100:
        print("你的寵物太胖死於三高QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[4] <=0:
        print("你的寵物餓死了QQ")
        print("生存天數:",day[0],"天")
        break
    elif Petlist[4] >=100:
        print("你的寵誤吃太多撐死了QQ")
        print("生存天數:",day[0],"天")
        break
    else:
        continue

