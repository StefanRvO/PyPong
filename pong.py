#!/usr/bin/python
import sys
import pygame
import os
import random
from pygame.locals import *
SCREENSIZE=(600,600)
class unit(object):
    def __init__ (self, sizex, sizey=None ,screensize=SCREENSIZE):
        self.x=sizex
        if sizey==None:
            self.y=self.x
        else:
            self.y=sizey
        self.gridsize=(screensize[0]/self.x,screensize[1]/self.y)
    def __str__ (self):
        return str(self.x)+"*"+str(self.y)
        
def ShowMenu():
    #Draw Title
    #print SCREENSIZE
    screen.fill((0,0,0))
    font=pygame.font.SysFont("Times New Roman",SCREENSIZE[0]/10)
    TitleText=font.render("PyPong",True,(255,255,255))
    
    screen.blit(TitleText,(SCREENSIZE[0]*0.5-TitleText.get_width()*0.5,SCREENSIZE[1]/10.-TitleText.get_height()*0.5))
    font=pygame.font.SysFont("Times New Roman",SCREENSIZE[0]/10)
    #Draw Start Button
    
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(float(SCREENSIZE[0])/10.,float(SCREENSIZE[1])*0.333,float(SCREENSIZE[0])/10.*2.5,float(SCREENSIZE[1])/7.),5)
    
    StartText=font.render("Start",True,(255,255,255))
    screen.blit(StartText,(float(SCREENSIZE[0])/10.+5,float(SCREENSIZE[1])*0.333+5))
    #Draw Opponent Button
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(float(SCREENSIZE[0])/10.*6,float(SCREENSIZE[1])*0.333,float(SCREENSIZE[0])/10.*3,float(SCREENSIZE[1])/7.),5)
    if Opponent:
        OpText=font.render("CPU",True,(255,255,255))
    else:
        OpText=font.render("Human",True,(255,255,255))
    screen.blit(OpText,(float(SCREENSIZE[0])/10.*6+5,float(SCREENSIZE[1])*0.333+5))
    #Draw Exit Button
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(float(SCREENSIZE[0])/10.*3.5,float(SCREENSIZE[1])*0.666,float(SCREENSIZE[0])/10.*2.5,float(SCREENSIZE[1])/7.),5)
    
    ExitText=font.render("Exit",True,(255,255,255))
    screen.blit(ExitText,(float(SCREENSIZE[0])/10.*3.5+5,float(SCREENSIZE[1])*0.666+5))
    
    pygame.display.flip()

def DrawGame():
    screen.fill((0,0,0))
    #Draw Points
    font=pygame.font.SysFont("Times New Roman",SCREENSIZE[0]/20)
    Point1=font.render("Player 1: "+str(Player1.points),True,(255,255,255))
    Point2=font.render("Player 2: "+str(Player2.points),True,(255,255,255))
    screen.blit(Point1,(5,5))
    screen.blit(Point2,(SCREENSIZE[0]-Point2.get_width()-5,5))
    #draw players
    Player1Rect=pygame.Rect(0,Player1.pos*U.y-(Player1.lenght/2)*SCREENSIZE[1],U.x,Player1.lenght*SCREENSIZE[1])
    pygame.draw.rect(screen,(255,255,255),Player1Rect)
    Player2Rect=pygame.Rect(SCREENSIZE[0]-U.x,Player2.pos*U.y-(Player2.lenght/2)*SCREENSIZE[1],U.x,Player2.lenght*SCREENSIZE[1])
    pygame.draw.rect(screen,(255,255,255),Player2Rect)
    #Draw ball
    BallRect=pygame.Rect((Ball1.pos[0]-Ball1.size/2.)*U.x,(Ball1.pos[1]-Ball1.size/2.)*U.x,Ball1.size*U.x,Ball1.size*U.y)
    pygame.draw.rect(screen,(255,255,0),BallRect)
    
    pygame.display.flip()
    
    
def EventQueueMenu():
    global State
    global Opponent
    ExitState=0
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                #check if we are within the buttons
                print event.pos
                if event.pos[0]>=float(SCREENSIZE[0])/10. and event.pos[0]<=float(SCREENSIZE[0])/10.*3.5 and event.pos[1]>=float(SCREENSIZE[1])*0.333 and event.pos[1]<=float(SCREENSIZE[1])*0.333+float(SCREENSIZE[1])/7.:
                    State=not(State)
                    
                elif event.pos[0]>=float(SCREENSIZE[0])/10.*6 and event.pos[0]<=float(SCREENSIZE[0])/10.*8.5 and event.pos[1]>=float(SCREENSIZE[1])*0.333 and event.pos[1]<=float(SCREENSIZE[1])*0.333+float(SCREENSIZE[1])/7.:
                    Opponent=not(Opponent)
                    print "o"
                elif event.pos[0]>=float(SCREENSIZE[0])/10.*3.5 and event.pos[0]<=float(SCREENSIZE[0])/10.*6 and event.pos[1]>=float(SCREENSIZE[1])*0.666 and event.pos[1]<=float(SCREENSIZE[1])*0.666+float(SCREENSIZE[1])/7.:
                    ExitState=not(ExitState)
                    
    return(State,Opponent,ExitState)    
    
def MenuState():
    global State
    global Opponent
    #print State
    while State==0:
        ShowMenu()
        EventResponse=EventQueueMenu()
        if EventResponse==0:
            continue
        else:
            State=EventResponse[0]
            Opponent=EventResponse[1]
            ExitOption=EventResponse[2]
            if ExitOption:
                sys.exit()
            
            

class Player:
    def __init__(self,Nr,Type):
        self.direction=0
        self.Nr=Nr
        self.speed=10
        self.Type=Type #0=human,1=CPU
        self.points=0
        self.pos=U.gridsize[1]/2
        self.lenght=0.1
    def PerformMove(self,Events):
        if self.Type==0:
            for event in Events:
                 if event.type==QUIT:
                    sys.exit()
                 if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        State=0
                    if self.Nr==1: #Player 1 key bindings
                        if event.key==K_UP:
                            self.direction=-1
                        if event.key==K_DOWN:
                            self.direction=1
                    if self.Nr==2:
                        if event.key==K_w:
                            self.direction-=1
                        if event.key==K_s:
                            self.direction+=1
                 if event.type==KEYUP:
                    if self.Nr==1:
                        if event.key==K_UP or event.key==K_DOWN:
                            self.direction=0
                    elif self.Nr==2:
                        if event.key==K_w or event.key==K_s:
                            self.direction=0
        if self.direction<=0:
            if not(self.pos<=U.gridsize[1]*(self.lenght/2.)):
                self.pos+=self.direction
        elif self.direction>=0:
            if not(self.pos>=U.gridsize[1]*(1.-self.lenght/2.)):
                self.pos+=self.direction
             
            
class Ball:
    def __init__(self):
        self.size=1
        self.directionvector=0
        self.pos=0
        self.Reset()
    def CheckPos(self):
        #Check if colliding with top or bottom, if so, change direction
        if self.pos[1]+self.size>=U.gridsize[1]:
            self.directionvector[1]=-abs(self.directionvector[1])
           # print 1.1
            return 0
        elif self.pos[1]-self.size<=0:
            self.directionvector[1]=abs(self.directionvector[1])
            #print 1
            return 0
        #Check if behind players
        if self.pos[0]-self.size<=0: #Player 2 scorred
            Player2.points+=1
            self.Reset()
            #print 2
            return 0
        elif self.pos[0]+self.size>=U.gridsize[0]: #Player 2 scorred
            Player1.points+=1
            self.Reset()
            #print 3
            return 0
        #check collision with players
        elif (self.pos[0]+self.size>=U.gridsize[0]-1 and (self.pos[1]<=Player2.pos+Player2.lenght/2*U.gridsize[1] and self.pos[1]>=Player2.pos-Player2.lenght/2*U.gridsize[1])):
            self.directionvector[0]=-self.directionvector[0] 
        elif(self.pos[0]-self.size*1.5<=0 and (self.pos[1]<=Player1.pos+Player1.lenght/2*U.gridsize[1] and self.pos[1]>=Player1.pos-Player1.lenght/2*U.gridsize[1])):
            self.directionvector[0]=-self.directionvector[0]
            
            #print 4
            return 0
        #print 5
        return 1
    def Move(self):
        directlenght=int((self.directionvector[0]**2+self.directionvector[1]**2)**0.5)+1
        steps=directlenght*2
        i=0
        while i<steps:
            self.pos[0]+=float(self.directionvector[0])/steps
            self.pos[1]+=float(self.directionvector[1])/steps
            i+=1
            if self.CheckPos()==0:
                break
    def Reset(self):
        options=[.2,-.2]
        self.pos=[U.gridsize[0]/2,U.gridsize[1]/2]
        self.directionvector=[random.choice(options),random.choice(options)]        
def GameState():
    #initialise players
    global Player1
    global Player2
    Player1=Player(1,0)
    Player2=Player(2,0)
    global Ball1
    Ball1=Ball()
    while True:
        time=clock.tick(200)
        print time
        events=pygame.event.get()
        Player1.PerformMove(events)
        Player2.PerformMove(events)
        Ball1.Move()
        DrawGame()
        

#initialize graphics
pygame.init()
U=unit(10)
screen=pygame.display.set_mode((U.gridsize[0]*U.x,U.gridsize[1]*U.y),0,32)
pygame.display.set_caption("PyPong","PyPong") #Set title
State=0 #0 is menu 1 is game
Opponent=0#0 is human, 1 is CPU
#initialise clock
clock=pygame.time.Clock()
clock2=pygame.time.Clock()
#GAMELOOP
while 1:
    if State==0:
        MenuState()
    elif State==1:
        GameState()
