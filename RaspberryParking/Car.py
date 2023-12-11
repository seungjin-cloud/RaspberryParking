import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Car:
    def __init__(self, width, height):
        self.up = Image.open('./images/Car/up.png').convert('RGBA')
        self.down = Image.open('./images/Car/down.png').convert('RGBA')
        self.left = Image.open('./images/Car/left.png').convert('RGBA')
        self.right = Image.open('./images/Car/right.png').convert('RGBA')
        self.appearance = self.up
        self.state = None
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])

    def setPos(self, x, y):
        self.position += np.array([x,y,x,y])    

    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command['up_pressed']:
                self.appearance = self.up 
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']:
                self.appearance = self.down
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']:
                self.appearance = self.left
                self.position[0] -= 5
                self.position[2] -= 5
                
            if command['right_pressed']:
                self.appearance = self.right
                self.position[0] += 5
                self.position[2] += 5

'''
    def move(self, command = None):
        if command == False:
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.outline = "#FF0000" #빨강색상 코드!

            if command['acc']:
                print('car acc')
                None
                
            if command['brake']:
                print('car brake')
                None
'''