#@title 28 野津祐太　NOTSUNDERTAE
"""""
#機能説明
プログラムが起動されると、タイトルと「はじめる」「とじる」が表示された画面が出てきます。
「はじめる」をクリックするとスタートです。矢印キーでソウル（ハート）を操作してください。
ひたすらブラスター攻撃（白いビーム）を避けてください。ＨＰが0になるとゲームオーバーです。
レベル200までいくとゲームクリアです。

#注意
このプログラムはおそらくgoogle Colaboratoryでは動きません。（画面を出せない）
VScodeやpythonのIDLE等なら動くと思います。
このプログラムは、同じフォルダーに画像や音声が入っていないと動きません。必ずフォルダーごと読み込んで実行してください。
"""""
import pygame
import sys
import random
# Pygameの初期化
pygame.init()
pygame.mixer.init()

#フレームレート設定
clock = pygame.time.Clock()
#画面設定
gamen = "title"
life = 99

# ウィンドウサイズの設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#タイトル
pygame.display.set_caption("NOTSUNDERTALE") 
#画像読み込み
title = pygame.image.load("title.png")
start = pygame.image.load("はじめる.png")
close = pygame.image.load("とじる.png")
startpoint = pygame.image.load("はじめるせんたく.png")
closepoint = pygame.image.load("とじるせんたく.png")
sanz_head= pygame.image.load("頭.png").convert()
sanz_chest= pygame.image.load("胴体.png")
sanz_leg= pygame.image.load("足.png")
fight1  = pygame.image.load("fight1.png")
fight2  = pygame.image.load("fight2.png")
act1  = pygame.image.load("ACT1.png")
act2 = pygame.image.load("ACT2.png")
item1 = pygame.image.load("ITEM1.png")
item2 = pygame.image.load("ITEM2.png")
mercy1 = pygame.image.load("MERCY1.png")
mercy2 = pygame.image.load("MERCY2.png")
mercy2 = pygame.image.load("MERCY2.png")
blaster1 = pygame.image.load("ブラスター１.png")
blaster2 = pygame.image.load("ブラスター２.png")
redsoul = pygame.image.load("redsoul.png")
bluesoul = pygame.image.load("bluesoul.png")

#画像の大きさ調整
title = pygame.transform.scale(title, (700, 550))
close = pygame.transform.scale(close, (250, 100)).convert_alpha()
start = pygame.transform.scale(start, (250, 100)).convert_alpha()
startpoint = pygame.transform.scale(startpoint, (250, 100)).convert_alpha()
closepoint = pygame.transform.scale(closepoint, (250, 100)).convert_alpha()
sanz_head = pygame.transform.scale(sanz_head, (75, 75)).convert_alpha()
sanz_chest = pygame.transform.scale(sanz_chest, (140, 75)).convert_alpha()
sanz_leg = pygame.transform.scale(sanz_leg, (110, 50)).convert_alpha()
fight1 = pygame.transform.scale(fight1, (150, 60)).convert_alpha()
fight2 = pygame.transform.scale(fight2, (150, 60)).convert_alpha()
act1 = pygame.transform.scale(act1, (150, 60)).convert_alpha()
act2 = pygame.transform.scale(act2, (150, 60)).convert_alpha()
item1 = pygame.transform.scale(item1, (150, 60)).convert_alpha()
item2 = pygame.transform.scale(item2, (150, 60)).convert_alpha()
mercy1 = pygame.transform.scale(mercy1, (150, 60)).convert_alpha()
mercy2 = pygame.transform.scale(mercy2, (150, 60)).convert_alpha()
blasterL1 = pygame.transform.scale(blaster1, (120, 60)).convert_alpha()
blasterL2 = pygame.transform.scale(blaster2, (120, 60)).convert_alpha()
redsoul = pygame.transform.scale(redsoul, (20, 20)).convert_alpha()
bluesoul = pygame.transform.scale(bluesoul, (20, 20)).convert_alpha()
blasterR1 = pygame.transform.flip(blasterL1, True, 0)
blasterR2 = pygame.transform.flip(blasterL2, True, 0)
blasterO1 = pygame.transform.rotate(blasterL1, -90)
blasterO2 = pygame.transform.rotate(blasterL2, -90)
blasterU1 = pygame.transform.rotate(blasterL1, 90)
blasterU2 = pygame.transform.rotate(blasterL2, 90)


#画像位置など設定
close_rect = close.get_rect(topleft=(275, 450))
start_rect = start.get_rect(topleft=(275, 300))
head_rect = sanz_head.get_rect(topleft=(362, 30))
chest_rect = sanz_chest.get_rect(topleft=(330, 90))
leg_rect = sanz_leg.get_rect(topleft=(350, 165))
fight1_rect = fight1.get_rect(topleft=(40, 520))
act1_rect = act1.get_rect(topleft=(230,520 ))
item1_rect = item1.get_rect(topleft=(420,520 ))
mercy1_rect = mercy1.get_rect(topleft=(610,520 ))
redsoul_rect = redsoul.get_rect(center=(400,400))


#フォントを読み込む
font = pygame.font.Font("misaki_gothic_2nd.ttf", 35)

#文字を用意
HP = font.render("player LV     HP", False, (255,255,255))

#BGMの読み込み
title_bgm = "Menu.wav"
battle_bgm = "Megalovania.wav"

#効果音の読み込み

se_damage = pygame.mixer.Sound("damage.wav")
se_break1 = pygame.mixer.Sound("break1.wav")
se_break2 = pygame.mixer.Sound("break2.wav")
se_blaster1 = pygame.mixer.Sound("ブラスター用意.wav")
se_blaster2 = pygame.mixer.Sound("ブラスター発射.wav")
se_win = pygame.mixer.Sound("win.wav")
se_gameover = pygame.mixer.Sound("gameover.wav")
se_ding = pygame.mixer.Sound("ding.wav")

# 効果音の音量調整
se_damage.set_volume(0.7)
se_break1.set_volume(0.7)
se_break2.set_volume(0.7)
se_blaster1.set_volume(0.3)
se_blaster2.set_volume(0.3)
se_win.set_volume(0.7)
se_gameover.set_volume(0.7)
se_ding.set_volume(0.5)

level = 0#レベル
gamen = "title"#画面の種類
soulplace = [0,0]#ソウルの情報（ゲームオーバーととき使用）

def play_bgm(filename, loop=-1, volume=0.5):#BGM流す
    pygame.mixer.music.stop()           # 再生中のBGMを停止
    pygame.mixer.music.load(filename)   # 新しいBGMを読み込み
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)       # ループ再生開始

class battle:#攻撃の司令塔
    def __init__(self):
        self.attackdirection = [] #ブラスターの向き
        self.fightrest = 0#攻撃のダウンタイム 
        self.fightnum = 0#攻撃が今どこまで進んだか
        self.nowfight = []#今行っている攻撃
        self.fight = []#攻撃のクラスのデータ
        self.attackinfo = []#すべての攻撃の情報
        self.num2 = 0 #プレイヤーの動く枠までの距離
        self.timespan = 0#攻撃までの時間
        for i in range(400):#ブラスターのデータを200個つくる
                self.attackdirection = []
                num = random.randint(0,3)
                if num == 0:
                    self.attackdirection.append("左")
                    self.num2 = 200
                elif num == 1:
                    self.attackdirection.append("右")
                    self.num2 = 200
                elif num == 2:
                    self.attackdirection.append("上")
                    self.num2 = 270
                elif num == 3:
                    self.attackdirection.append("下")
                    self.num2 = 270
                distance = random.randint(0,200)#場所をランダムに出す
                self.attackdirection.append(distance+self.num2)
                self.attackinfo.append(self.attackdirection)

                temp = blaster(self.attackinfo[i][0],self.attackinfo[i][1])
                self.fight.append(temp)#リストにブラスターのクラスデータを入れる。


    def update(self):
        global level
        if self.fightrest >= 50 and self.fightnum < 200:#ダウンタイムを満たしレベル200以内なら攻撃を追加する
            self.nowfight.append(self.fight[self.fightnum])
            self.fightnum += 1
            self.fightrest = 0
            
        for i in self.nowfight:#ブラスターを更新する
            self.delete = i.update()
            if self.delete: #攻撃が終わったブラスターのデータを削除する
                self.nowfight.remove(i)

        #攻撃の難易度（頻度調整）
        if self.fightnum <= 10:
            self.timespan = 1
        elif self.fightnum <= 30:
            self.timespan = 2
        elif self.fightnum <= 75:
            self.timespan = 3
        elif self.fightnum <= 150:
            self.timespan = 4
        elif self.fightnum <= 200:
            self.timespan = 5
        #ダウンタイムを更新する
        self.fightrest = min(self.fightrest+random.randint(1,self.timespan),70)
        level = self.fightnum#グローバル変数でレベルの数値が全体で使えるようにする

class blaster:#ブラスターの動き
    def __init__(self,direction,position):
        self.direction = direction
        #ブラスターの向きと位置を確定する
        if self.direction == "上":
            self.x = position
            self.y = 0
        elif self.direction == "下":
            self.x = position
            self.y = 600
        elif self.direction == "右":
            self.x = 800
            self.y = position
            self.form = blasterR1
        elif self.direction == "左":
            self.x = 0
            self.y = position
            self.form = blasterL1
        self.back = False
        self.show = True
        self.dam = damage()
        self.obstacles = (0,0,0,0)
        self.sound = True


    def update(self):
        #向きごとの動きを更新する
        if self.direction == "左":
            if not(self.back):
                if 170 >= self.x:#進む
                    self.x = min(self.x+9,180)
                    self.form = blasterL1
                else:#ある座標に達したら、攻撃する
                    #ビームとなる四角を描く
                    self.obstacles= pygame.draw.rect(screen, (255, 255, 255), (self.x+60,self.y+15, 1000, 30))
                    self.form = blasterL2
                    self.back = True
                    self.sound = True

            else:#打ちながら帰る
                if 0 <= self.x:
                    self.x = max(self.x-15,-1)
                    self.obstacles = pygame.draw.rect(screen, (255, 255, 255), (self.x+60,self.y+15, 1000, 30))
                else:#ある座標に達したら、消える
                    self.show = False
                    self.obstacles = (0,0,0,0)
                    return True


        if self.direction == "右":
            if not(self.back):
                if 550 <= self.x:
                    self.x = max(self.x-10,540)
                    self.form = blasterR1

                else:
                    self.obstacles= pygame.draw.rect(screen, (255, 255, 255), (0,self.y+15, self.x+30, 30))
                    self.form = blasterR2
                    self.back = True
                    self.sound = True
            else:
                if 800 >= self.x:
                    self.x = min(self.x+15,801)
                    self.obstacles = pygame.draw.rect(screen, (255, 255, 255), (0,self.y+15, self.x+30, 30))
                else:
                    self.show = False
                    self.obstacles = (0,0,0,0)
                    return True


        if self.direction == "上":
            if not(self.back):
                if 90 >= self.y:
                    self.y = min(self.y+4,100)
                    self.form = blasterO1

                else:
                    self.obstacles= pygame.draw.rect(screen, (255, 255, 255), (self.x+15,self.y+30, 30, 800))
                    self.form = blasterO2
                    self.back = True
                    self.sound = True
            else:
                if 0 <= self.y:
                    self.y = max(self.y-15,-1)
                    self.obstacles = pygame.draw.rect(screen, (255, 255, 255), (self.x+15,self.y+30, 30, 800))
                else:
                    self.show = False
                    self.obstacles = (0,0,0,0)
                    return True

        if self.direction == "下":
            if not(self.back):
                if 460 <= self.y:  # 下から出てくる動き
                    self.y = max(self.y-5, 450)
                    self.form = blasterU1  # 下向き画像
                else:
                    self.obstacles = pygame.draw.rect(screen, (255, 255, 255), (self.x+15, 0, 30, self.y+30))
                    self.form = blasterU2
                    self.back = True
                    self.sound = True
            else:
                if 600 >= self.y:
                    self.y = min(self.y+15, 610)
                    self.obstacles = pygame.draw.rect(screen, (255, 255, 255), (self.x+15, 0, 30, self.y+30))
                else:
                    self.show = False
                    self.obstacles = (0,0,0,0)
                    return True
        #音を鳴らす
        if self.sound:
            if self.form == blasterU1 or self.form == blasterO1 or self.form == blasterL1 or self.form == blasterR1:
                se_blaster1.play()
                self.sound = False
            else:
                se_blaster2.play()
                self.sound = False
        #ブラスターを表示する
        if self.show:
            screen.blit(self.form,(self.x,self.y))
        self.dam.update(redsoul_rect,self.obstacles)#ソウルとぶつかったか判定するdefを呼び出す

class damage:#攻撃とソウルがぶつかったかを判定し、ライフを削る
    def __init__(self):
        self.downtime = 26
    def update(self,soul,enemy):
        global life
        if self.downtime > 25:
            if soul.colliderect(enemy):
                life -= 10
                self.downtime = 0
                se_damage.play()
        self.downtime = min(self.downtime+1,26)

class Soul:#ソウルの動き
    def __init__(self):
        self.jump = True
        self.soulREDBLUE = "red"
        self.onlyone = True
    def move(self,keys):
        global soulplace
        if level <= 150 :#レベル150以下なら赤ソウル、それ以上なら青ソウル
            self.soulREDBLUE = "red"
        else:
            self.soulREDBLUE = "blue"
            if self.onlyone:
                se_ding.play()#音を鳴らす
                self.onlyone = False
        if self.soulREDBLUE == "red":#赤のときの動き
            redsoul_rect.y = self.control("y","red",redsoul_rect.y,keys)
            redsoul_rect.x = self.control("x","red",redsoul_rect.x,keys)
            screen.blit(redsoul,redsoul_rect)
            
        if self.soulREDBLUE == "blue":#青の時の動き
            redsoul_rect.y = self.control("y","blue",redsoul_rect.y,keys)
            redsoul_rect.x = self.control("x","blue",redsoul_rect.x,keys)
            screen.blit(bluesoul,redsoul_rect)
        soulplace[0] = redsoul_rect#グローバル変数で座標を共有する
        soulplace[1] = self.soulREDBLUE
    def control(self,xy,RB,now,keys):#キー入力を読み取り、座標の数値を変える
        if xy == "x":#左右
            if keys[pygame.K_LEFT]: 
                now = max(302,now-10)
            if keys[pygame.K_RIGHT]: 
                now = min(478,now+10)
        if RB == "red":#上下
            if xy == "y":
                if keys[pygame.K_UP]: 
                    now = max(232,now-10)
                if keys[pygame.K_DOWN]: 
                    now = min(408,now+10)
        if RB == "blue":#重力があるときの上下
            if xy == "y":
                if now <= 240:
                    self.jump = False
                if keys[pygame.K_UP]and self.jump: 
                    now = max(232,now-10)
                else:
                    now = min(408,now+10)
                    self.jump = False
                    if now > 401:
                        self.jump = True
        return now # 座標の数値を返す

class Lifegage:#ライフゲージ
    def update(self):
        global life,level
        #赤と黄色の境目
        sakaime = life*2
        # 残り部分の長方形を描画
        pygame.draw.rect(screen, (255, 255, 0), (300, 460, sakaime, 30))
        # 減った部分の長方形を描画
        pygame.draw.rect(screen, (255, 0, 0), (sakaime+300,460 ,499-(sakaime+300) , 30))
        #残りライフの数字やレベルを表示
        life_num = font.render(str(int(life))+" / 99", False, (255,255,255))
        level_num = font.render(str(int(level)), False, (255,255,255))
        screen.blit(life_num, (550, 460))
        screen.blit(level_num, (200, 460))
        screen.blit(HP, (10, 460))
        #四角を表示
        pygame.draw.rect(screen, (255,255,255), (300, 230, 200, 200), 3)

class Sans:#サンズの動き
    def __init__(self):
        self.sanz_RL = "right"
        self.sanz_x = 363
        self.sanz_y = 0
    def update(self):
        #サンズX座標設定
        if self.sanz_RL == "right":
            self.sanz_x += 0.2
        else:
            self.sanz_x -= 0.2
        if self.sanz_x > 364:#364
            self.sanz_RL = "left"
        elif self.sanz_x < 362:#362
            self.sanz_RL = "right"
        #サンズY座標設定
        self.sanz_y = 0.77*(self.sanz_x - 363)**2 + 30

        #座標反映
        head_rect.x = self.sanz_x
        head_rect.y = self.sanz_y
        chest_rect.x = self.sanz_x-35
        chest_rect.y = self.sanz_y+60

        screen.blit(sanz_leg,leg_rect)
        screen.blit(sanz_chest,chest_rect)
        screen.blit(sanz_head,head_rect)

class judgement:#ゲームクリア、ゲームオーバーかを判定
    def __init__(self):
        self.clearspan = 0
    def update(self):
        global level,gamen
        gamen = "game"
        if level >= 200:#レベル200なら、ゲームクリア
            self.clearspan += 1
        if life <= 0:#ライフが0なら、ゲームオーバー
            gamen = "lose"


        if self.clearspan >= 100:
            gamen = "clear"

class Game:#ゲーム時の司令塔
    def __init__(self):#各クラスを呼び出す
        self.attacknumber = 0#攻撃が何番目まで進んだか  
        self.soul = Soul()
        self.lifegage = Lifegage()
        self.sans = Sans()
        self.battle = battle()
        self.judge = judgement()
    def update(self,keys):
        #下の飾りを表示
        screen.blit(fight1,fight1_rect)
        screen.blit(act1,act1_rect)
        screen.blit(item1,item1_rect)
        screen.blit(mercy1,mercy1_rect)
        #各クラスを更新する
        self.soul.move(keys)
        self.lifegage.update()
        self.sans.update()
        self.battle.update()
        self.judge.update()

class Start:#スタート画面
    def update(self,event,mouse_pos):
        global gamen
        #画像はる
        screen.blit(title, (50,-150))

        #閉じるボタン判定
        if close_rect.collidepoint(mouse_pos):
            screen.blit(closepoint, close_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        else:
            screen.blit(close, close_rect)
        #始めるボタン判定
        if start_rect.collidepoint(mouse_pos):
            screen.blit(startpoint,start_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                gamen = "game"
                play_bgm(battle_bgm)#バトル用のBGMを流す
        else:
            screen.blit(start, start_rect)

class clear:#クリア画面
    def __init__(self):
        self.onlyone = True
    def update(self):
        if self.onlyone:#音楽流す
            pygame.mixer.music.stop()
            se_win.play()
            self.onlyone = False
        #gameclearの文字を表示
        winfon = font.render("GAME CLEAR", False, (255,255,255))
        screen.blit(winfon, (300, 300)) 

class lost:#ゲームオーバー画面
    def __init__(self):
        self.onlyone = True
        self.count = 0
        self.downtime = 0
    def update(self):
        global soulplace,level
        #ピッ→真っ暗→gameoverの動き
        if self.count == 0:
            
            if self.onlyone:
                pygame.mixer.music.stop()
                se_break1.play()
                self.onlyone = False

            if soulplace[1] == "red":
                screen.blit(redsoul,soulplace[0])
                
            elif soulplace[1] == "blue":
                screen.blit(bluesoul,soulplace[0])

            if self.downtime >= 30:
                self.count = 1
                self.onlyone = True
            else:
                self.downtime += 1
        
        if self.count == 1:
            if self.onlyone:
                pygame.mixer.music.stop()
                se_break2.play()
                self.onlyone = False
            if self.downtime >= 90:
                self.count = 2
                self.onlyone = True
            else:
                self.downtime += 1

        if self.count == 2:
            if self.onlyone:
                pygame.mixer.music.stop()
                self.onlyone = False
                se_gameover.play()#音楽流す
            
            #gameoverとレベルの表示
            losefon = font.render("GAME OVER", False, (255,255,255))
            levelfon = font.render("your level is "+str(level) , False, (255,255,255))
            screen.blit(losefon, (300, 300)) 
            screen.blit(levelfon, (400, 500)) 

#最初に使うクラスを呼び出す
begin = Start()
game = Game()
win = clear()
lose = lost()
play_bgm(title_bgm)#最初のBGMを流す
while True:#すべての根本となる司令塔
    #マウスの情報取得
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()  

    for event in pygame.event.get():#×を押すと閉じる
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 画面を黒で塗りつぶす
    screen.fill((0, 0, 0))
    #ゲームの画面を変更
    
    if gamen == "title":
        begin.update(event,mouse_pos)
    
    elif gamen == "game":
        game.update(keys)

    elif gamen == "clear":
        win.update()

    elif gamen == "lose":
        lose.update()
    
    
    
    # 画面の更新
    pygame.display.flip()
    pygame.display.update()
    # フレームレートを30FPSに固定
    clock.tick(30)