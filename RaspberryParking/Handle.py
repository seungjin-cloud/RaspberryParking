'''
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Handle:
    def __init__(self, width, height):
        self.appearance = Image.open('./images/handle.png').convert('RGBA')
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.angle = 0


    def setPos(self, x, y):
        self.position += np.array([x,y,x,y])
        
    def rotate(self, angle,direction):
        radians = np.radians(angle)
        center = np.array([self.position[0] - 100, self.position[1] - 100])
        if direction == 'left':
            rotated_position = np.array([
                (self.position[0] - center[0]) * np.cos(radians) - (self.position[1] - center[1]) * np.sin(radians) + center[0],
                (self.position[0] - center[0]) * np.sin(radians) + (self.position[1] - center[1]) * np.cos(radians) + center[1],
                (self.position[2] - center[0]) * np.cos(radians) - (self.position[3] - center[1]) * np.sin(radians) + center[0],
                (self.position[2] - center[0]) * np.sin(radians) + (self.position[3] - center[1]) * np.cos(radians) + center[1]
            ])
        else:
            rotated_position = np.array([
                (self.position[0] - center[0]) * np.cos(radians) + (self.position[1] - center[1]) * np.sin(radians) + center[0],
                -(self.position[0] - center[0]) * np.sin(radians) + (self.position[1] - center[1]) * np.cos(radians) + center[1],
                (self.position[2] - center[0]) * np.cos(radians) + (self.position[3] - center[1]) * np.sin(radians) + center[0],
                -(self.position[2] - center[0]) * np.sin(radians) + (self.position[3] - center[1]) * np.cos(radians) + center[1]
            ])


    def rotation(self,command = None):
        if command['left']:
            if(self.angle > -45):
                self.angle -= 0.1
                self.rotate(self.angle,'left')
                print("left")
            
        if command['right']:
            if(self.angle < 45):
                self.angle += 0.1
                self.rotate(self.angle,'right')
                print("right")
            

'''