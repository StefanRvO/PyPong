#!/usr/bin/python
import sys
import pygame
import os
from pygame.locals import *

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
            
            


def GameState():
    print "Game"
    

SCREENSIZE=(600,600)
#initialize graphics
pygame.init()
screen=pygame.display.set_mode(SCREENSIZE,0,32) 
pygame.display.set_caption("PyPong","PyPong") #Set title
State=0 #0 is menu 1 is game
Opponent=0#0 is human, 1 is CPU
#initialise clock
clock=pygame.time.Clock()
#GAMELOOP
while 1:
    if State==0:
        MenuState()
    elif State==1:
        GameState()
