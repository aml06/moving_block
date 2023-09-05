# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:34:27 2023

@author: 18019
"""

import pygame
import sys
import math

def __main__():
    pygame.init()
    WIDTH, HEIGHT = 1000, 1000
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255, 36, 0)
    BLUE = (0, 0, 255)
    pygame.key.set_repeat(5,50)
    running = True
    rect = Rectangle(100,100,50,50, WHITE)
    rect.multiplier = 50
    blockList = []
    collideList = []
    y_no_repeat = True
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
                    #dynamic block cannot be in same coordinates as a collision block
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkDown(rect, i):
                                collision == False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveDown()
                if event.key == pygame.K_w:
                    print("'W' key is pressed")
                    #dynamic block cannot be in same coordinates as a collision block
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkUp(rect, i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveUp()
                if event.key == pygame.K_a:
                    print("'A' key is pressed")
                    #dynamic block cannot be in same coordinates as a collision block
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkLeft(rect,i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveLeft()
                if event.key == pygame.K_d:
                    print("'D' key is pressed")
                    #dynamic block cannot be in same coordinates as a collision block
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkRight(rect,i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveRight()
                    
                #Program quits with escape
                if event.key == pygame.K_ESCAPE:
                    print("'Esc' key is pressed")
                    running = False
                    
                #arrow keys also work to move
                if event.key == pygame.K_DOWN:
                    print("'Down Arrow' key is pressed")
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkDown(rect,i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveDown()
                
                if event.key == pygame.K_UP:
                    print("'UP Arrow' key is pressed")
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkUp(rect, i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveUp()

                if event.key == pygame.K_LEFT:
                    print("'Left Arrow' key is pressed")
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkLeft(rect,i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
                        rect.moveLeft()

                if event.key == pygame.K_RIGHT:
                    print("'Right Arrow' key is pressed")
                    collision = False
                    for i in collideList:
                        if rect.colliderect(i):
                            collision = True
                            if checkRight(rect,i):
                                collision = False
                            print("Avoiding Collision!")
                    if collision == False:
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
                    
                if event.key == pygame.K_y:
                    if y_no_repeat:
                        print("'Y' key is pressed")
                        
                        block = Rectangle(rect.position()[0], rect.position()[1], 50, 50, BLUE)
                        collideList.append(block)
                        '''
                        if rect.position()[0] > WIDTH // 2:
                            rect.changePosition(rect.position()[0]-20, rect.position()[1])
                        else:
                            rect.changePosition(rect.position()[0]+20, rect.position()[1])
                            
                        if rect.position()[1] > HEIGHT // 2:
                            rect.changePosition(rect.position()[0], rect.position()[1] - 20)
                        else:
                            rect.changePosition(rect.position()[0], rect.position()[1] + 20)
                        '''
                        y_no_repeat = False
                    else:
                        print("Prevented repeat 'Y'")
                    
                #move faster when e is pressed, slower when q is pressed
                if event.key == pygame.K_e:
                    print("'E' key is pressed")
                    rect.changeMultiplier(2)
                if event.key == pygame.K_q:
                    print("'Q' key is pressed")
                    rect.changeMultiplier(-2)
                    
                if event.key == pygame.K_u:
                    print("'U' key is pressed")
                    collideList = []
                    
                if event.key == pygame.K_n:
                    print("Status Key pressed")
                    print("------------------------")
                    print(f"Collision List: {collideList}")
                    print(f"Block List: {blockList}")
                    
            #Making a static block the dynamic block will collide with / be unable to pass through
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    print("'Y' key is released")
                    y_no_repeat = True
                    \
                
        
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
        for brick in collideList:
            brick.draw(window)
        pygame.display.update()
    
    #exit while loop, program stops
    pygame.quit()
    sys.exit()
    
#Rectangle class, used for both dynamic and static blocks
class Rectangle(pygame.Rect):
    def __init__(self, x, y, width, height, color, multiplier = 10):
        super().__init__(x,y,width, height)
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
    
def checkDown(rect1, rect2):
    if rect1.position()[1] >= rect2.position()[1]:
        return False
    else:
        return True

def checkUp(rect1, rect2):
    if rect1.position()[1] < rect2.position()[1]:
        return False
    else:
        return True

def checkLeft(rect1, rect2):
    if rect1.position()[0] >= rect2.position()[0]:
        return False
    else:
        return True

def checkRight(rect1, rect2):
    if rect1.position()[0] < rect2.position()[0]:
        return False
    else:
        return True
    
__main__()
