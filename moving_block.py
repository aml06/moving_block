# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:34:27 2023

@author: 18019
"""

import pygame
import sys

def __main__():
    pygame.init()
    WIDTH, HEIGHT = 1000, 1000
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255, 36, 0)
    pygame.key.set_repeat(5,50)
    running = True
    rect = Rectangle(100,100,50,50, WHITE)
    rect.multiplier = 50
    blockList = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                new_width, new_height = event.size
                WIDTH, HEIGHT = new_width, new_height
                window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                #move using awsd
                if event.key == pygame.K_s:
                    print("'S' key is pressed")
                    rect.moveDown()
                if event.key == pygame.K_w:
                    print("'W' key is pressed")
                    rect.moveUp()
                if event.key == pygame.K_a:
                    print("'A' key is pressed")
                    rect.moveLeft()
                if event.key == pygame.K_d:
                    print("'D' key is pressed")
                    rect.moveRight()
                    
                #Program quits with escape
                if event.key == pygame.K_ESCAPE:
                    print("'Esc' key is pressed")
                    running = False
                    
                #arrow keys also work to move
                if event.key == pygame.K_DOWN:
                    print("'Down Arrow' key is pressed")
                    rect.moveDown()
                
                if event.key == pygame.K_UP:
                    print("'UP Arrow' key is pressed")
                    rect.moveUp()

                if event.key == pygame.K_LEFT:
                    print("'Left Arrow' key is pressed")
                    rect.moveLeft()

                if event.key == pygame.K_RIGHT:
                    print("'Right Arrow' key is pressed")
                    rect.moveRight()
                    
                #generate red square when we hit enter at the present controllable rectangle location
                if event.key == pygame.K_RETURN:
                    print("'Enter' key is pressed")
                    block = Rectangle(rect.position()[0], rect.position()[1], 50, 50, RED)
                    blockList.append(block)
                    
                #clear all red rectangles when 'c' is pressed.
                if event.key == pygame.K_c:
                    print("'C' key is pressed")
                    blockList = []
                    
                #move faster when e is pressed, slower when q is pressed
                if event.key == pygame.K_e:
                    print("'E' key is pressed")
                    rect.changeMultiplier(2)
                if event.key == pygame.K_q:
                    print("'Q' key is pressed")
                    rect.changeMultiplier(-2)
        
        #So controllable rectangle stays inside screen, will now warp to other side when edge is hit, works with resize
        if rect.position()[0] < 0:
            rect.changePosition(WIDTH,rect.position()[1])
        if rect.position()[1] < 0:
            rect.changePosition(rect.position()[0],HEIGHT)
        if rect.position()[0] > WIDTH:
            rect.changePosition(0,rect.position()[1])
        if rect.position()[1] > HEIGHT:
            rect.changePosition(rect.position()[0],0)
        
        #render on screen
        window.fill(BLACK)
        rect.draw(window)
        for block in blockList:
            block.draw(window)
        pygame.display.update()
    
    #exit while loop, program stops
    pygame.quit()
    sys.exit()
    
#Rectangle class, used for both dynamic and static blocks
class Rectangle:
    def __init__(self, x, y, width, height, color, multiplier = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.multiplier = multiplier
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        
    def moveDown(self):
        self.y = self.y + self.multiplier
        
    def moveUp(self):
        self.y = self.y - self.multiplier
        
    def moveLeft(self):
        self.x = self.x - self.multiplier
        
    def moveRight(self):
        self.x = self.x + self.multiplier
    
    def changeMultiplier(self, num):
        self.multiplier = self.multiplier + num
    
    def position(self):
        return [self.x, self.y]
    
    def changePosition(self,x,y):
        self.x = x
        self.y = y
    
__main__()
