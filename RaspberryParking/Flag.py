import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Flag:
    def __init__(self,width, height):
        self.appearance = Image.open('./images/flag.png').convert('RGBA')
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.outline = "#00FF00"
        
    def setPos(self, x, y):
        self.position += np.array([x,y,x,y]) 
