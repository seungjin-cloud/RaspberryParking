from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

class Background:
    def __init__(self):
        self.background_list = [] 
        background = Image.open('./images/background/1(start).png').convert('RGBA')
        self.background_list.append(background)
        background = Image.open('./images/background/2.png').convert('RGBA')
        self.background_list.append(background)
        background = Image.open('./images/background/3(end).png').convert('RGBA')
        self.background_list.append(background)

    def step(self, params, background):
        if params['stage'] == 2:
            background = self.background_list[1]
        elif params['stage'] == 3:
            background = self.background_list[2]

        return background

            