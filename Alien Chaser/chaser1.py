# Made By Biruduganti Praveen
import pygame
import random
import math
import time
import tkinter
from tkinter import messagebox


class Chaser:
    def __init__(self):
        
        pygame.display.set_icon(pygame.image.load('Icons\\icon.png'))
        pygame.display.set_caption('Alien Chaser')
        # scr.fill((255,0,0))
        self.running=True
        #----shooter----<
        self.shooterX = 235
        self.shooterY = 500
        self.shooterX1 = 0
        self.shooterY1 = 0
        #----Enemy-------<
        self.enemyImg = []
        self.enemyX = [] 
        self.enemyY = []
        self.enemyX1 = []
        self.enemyY1 = []
        self.enemyBullet = []
        self.enemyBulY=0
        self.bulY1=[]
        self.enemybulX=0
        #---bullet----<
        self.bulletY = 500
        self.bulletX = 0
        self.bulletX1 = 0
        self.bulletY1 = 30
        self.bulletState = 'Ready'
        #-----score----<
        self.score_value=0
        self.wallpapers=[]
        self.j=0

    def message(self,scr):
        # scr.blit(pygame.image.load('Icons\\blast.png'),(self.shooterX,self.shooterY))
        window=tkinter.Tk()
        window.eval('tk::PlaceWindow %s center'%window.winfo_toplevel())
        window.withdraw()
        if messagebox.askyesno('Question','Do you want to Play Again')==True:
            self.__init__()
            self.main(scr)
        else:
            return False
    
    def wallpaper(self):
        for i in range(18):
            self.wallpapers.append(pygame.image.load(f'wal1\\frame_{i}_delay-0.07s.gif'))


    def score(self, scr):
        font=pygame.font.Font('freesansbold.ttf',32)
        score=font.render('Score: '+ str(self.score_value),True, (255,255,255),(200,100))
        scr.blit(score,(10,10))
    
    def over(self,scr):
        font = pygame.font.Font('freesansbold.ttf',32)
        game=font.render('Game Over',True, (230,220,170))
        a=True
        while a:
            scr.blit(pygame.image.load('Icons\\bgover.png'),(0,0))
            scr.blit(game,(200,int(600/2)))
            scr.blit(font.render('Press F9 to Play Again',True, (0,200,0)),(100,400))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F9:
                            self.__init__()
                            self.main(scr)
            pygame.display.update()
        # return False
        
        
    def shooter(self, x, y, scr):
        if x <= 0:
            x = 0
        elif x >= 500:
            x = 500
        elif y <= 400:
            y=400
        elif y >= 550:
            y=550
        scr.blit(pygame.image.load('Icons\\rocket1.png'), (x, y))

    def enemy(self):
        for i in range(8):
            self.enemyImg.append(pygame.image.load('Icons\\alien.png'))
            self.enemyX.append(random.randint(0, 500))
            self.enemyY.append(random.randint(5, 60))
            self.enemyX1.append(10)
            self.enemyY1.append(40)
            self.bulY1.append(2)
            self.enemyBullet.append(pygame.image.load('Icons\\BlueBar1.jpg')) 

    def bullet(self, x, y, scr):
        self.bulletState='fire'
        scr.blit(pygame.image.load('Icons\\bullet (1).png'), (x+8, y))

    def collision_e_b(self, X, Y, i):
        dist=math.sqrt((self.enemyX[i]-X)**2+(self.enemyY[i]-Y)**2)
        if dist <=30: return True
        else: return False

    def collision_E_S(self, x, y, i):
        dist = math.sqrt((x-self.enemyX[i])**2+(y-self.enemyY[i])**2)
        if dist <= 35: return True
        else: return False
    
    def collision_enemyBul_S(self,enemybulX,enemyBulY,shooterX,shooterY):
        dist=math.sqrt((enemybulX-shooterX)**2+(enemyBulY-shooterY)**2)
        if dist <=24 : 
            scr.blit(pygame.image.load('Icons\\blast.png'),(self.shooterX,self.shooterY))
            return True
        else: return False

    def main(self, scr):
        self.enemy()
        self.enemybulX=self.enemyX[random.randint(0,7)]

        while self.running:
            scr.blit(pygame.image.load('Icons\\bg.png'),(0,0))
            scr.blit(pygame.image.load('Icons\\BlueBar1.jpg'),(self.enemybulX+15,self.enemyBulY+12))
            self.enemyBulY+=24

            if self.enemyBulY>=600:
                self.enemyBulY=self.enemyY[random.randint(0,7)]  
                self.enemybulX=self.enemyX[random.randint(0,7)]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                #---Shooter Movement------<
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_F9:
                    #     self.__init__()
                    #     self.main(scr)
                    if event.key == pygame.K_LEFT:
                        self.shooterX1 -= 15
                    if event.key == pygame.K_RIGHT:
                        self.shooterX1 += 15
                    if event.key == pygame.K_UP:
                        self.shooterY1-=15
                    if event.key == pygame.K_DOWN:
                        self.shooterY1+=15
                    if event.key == pygame.K_SPACE:
                        if self.bulletState == 'Ready':
                            self.bulletX = self.shooterX
                            self.bulletY = self.shooterY
                            self.bullet(self.bulletX, self.bulletY, scr)
                if event.type == pygame.KEYUP:
                    self.shooterX1 = 0
                    self.shooterY1 = 0 
            self.shooterX += self.shooterX1
            self.shooterY += self.shooterY1
            self.shooter(self.shooterX, self.shooterY, scr)

            # ------Enemy-----<
            for i in range(8):
                self.enemyX[i] += self.enemyX1[i]
                if self.enemyX[i] <= 0:
                    self.enemyX1[i] = 14
                    self.enemyY[i] += self.enemyY1[i]
                elif self.enemyX[i] >= 500:
                    self.enemyX1[i] =- 14
                    self.enemyY[i] += self.enemyY1[i]
                scr.blit(self.enemyImg[i], (self.enemyX[i], self.enemyY[i]))

                #-------collision of bullet and enemy--------<
                col = self.collision_e_b(self.bulletX, self.bulletY, i)
                if self.bulletState == 'fire':
                    if col:
                        scr.blit(pygame.image.load('Icons\\blast.png'),(self.bulletX,self.bulletY))
                        self.score_value += 1
                        self.bulletY = 500
                        self.bulletState='Ready'
                        self.enemyX[i] = random.randint(0,500)
                        self.enemyY[i] = random.randint(5,60)

                #-------collision of Shooter and enemy--------<
                col2 = self.collision_E_S(self.shooterX, self.shooterY, i)
                if col2:
                    # scr.blit(pygame.image.load('Icons\\bgover.png'),(550,600))
                    scr.blit(pygame.image.load('Icons\\blast.png'),(self.shooterX,self.shooterY))
                    self.over(scr)
                    # 
                    self.running=False

                #------Collision of Bottom and Enemy--------<
                if self.enemyY[i] >= 600:
                    self.enemyX[i] = random.randint(0,500)
                    self.enemyY[i] = random.randint(5,60)

                #-------Collision of EnemyBul and Shooter-------<
                col3= self.collision_enemyBul_S(self.enemybulX,self.enemyBulY,self.shooterX,self.shooterY) 
                if col3:
                    scr.blit(pygame.image.load('Icons\\bgover.png'),(550,600))
                    scr.blit(pygame.image.load('Icons\\blast.png'),(self.shooterX,self.shooterY))
                    # scr.blit(pygame.image.load('Icons\\bgover1.jpg'),(550,600))
                    self.over(scr)
                    self.running = False
                    # break
            
            #--------Shooter Bullet------<
            if self.bulletY <= 0:
                self.bulletY = 480
                self.bulletState = 'Ready'
            if self.bulletState == 'fire':
                self.bullet(self.bulletX, self.bulletY, scr)
                self.bulletY -= self.bulletY1

            self.score(scr)
            self.j+=1
            pygame.display.update()
            time.sleep(0.08)
        

if __name__ == "__main__":
    pygame.init()
    scr = pygame.display.set_mode((550, 600))
    p1 = Chaser()
    p1.main(scr)
