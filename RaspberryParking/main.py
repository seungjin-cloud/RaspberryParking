from PIL import Image, ImageDraw, ImageFont
import time
import random
import numpy as np
from colorsys import hsv_to_rgb
from Car import Car
from Obstacle import Obstacle
from Flag import Flag
#from Handle import Handle
from Joystick import Joystick
from Background import Background

def check_collision(car, obstacle):
    # Check for collision between the car and obstacle bounding boxes
    car_left, car_top, car_right, car_bottom = car.position
    obstacle_left, obstacle_top, obstacle_right, obstacle_bottom = obstacle.position

    if (car_right > obstacle_left and
        car_left < obstacle_right and
        car_bottom > obstacle_top and
        car_top < obstacle_bottom):
        return True  # Collision detected
    else:
        return False  # No collision

def check_clear(car, flag):
    # Check for collision between the car and obstacle bounding boxes
    car_left, car_top, car_right, car_bottom = car.position
    flag_left, flag_top, flag_right, flag_bottom = flag.position

    if (car_right > flag_left and
        car_left < flag_right and
        car_bottom > flag_top and
        car_top < flag_bottom):
        return True  # Collision detected
    else:
        return False  # No collision


def main(Joystick,Background):
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    my_Car = Car(joystick.width, joystick.height)
    obstacle = Obstacle(joystick.width, joystick.height)
    flag = Flag(joystick.width, joystick.height)
    #my_Handle = Handle(joystick.width,joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    background = Background.background_list[0]
    my_Car.setPos(50,90)
    obstacle.setPos(-90,90)
    flag.setPos(100,-100)
    #my_Handle.setPos(-100,100)

    while True:
        # collision event
        if check_collision(my_Car, obstacle):
            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
            end = Image.open("./images/end.png").convert('RGBA')
            end = end.resize((241, 241)) 
            my_image.paste(end, (0, 0))
            joystick.disp.image(my_image)
            break

        if check_clear(my_Car, flag):
            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
            end = Image.open("./images/clear.png").convert('RGBA')
            end = end.resize((241, 241)) 
            my_image.paste(end, (0, 0))
            joystick.disp.image(my_image)
            break

        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        



        '''
        command = {'left': False, 'right': False, 'acc': False, 'brake': False}
        
        # 핸들
        if not joystick.button_L.value:  # 왼쪽 버튼 (좌회전)
            command['left'] = True  # 좌회전 각도 설정 
            print('left')

        if not joystick.button_R.value:  # 오른쪽 버튼 (우회전)
            command['right'] = True  # 우회전 각도 설정 
            print('right')

        if not joystick.button_A.value:  # A 버튼 (가속)
            command['acc'] = True
            print('acc')

        if not joystick.button_B.value:  # B 버튼 (브레이크)
            command['brake'] = True
            print('brake')

        #my_Handle.rotation(command)
        '''
        my_Car.move(command)
        
    
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        background = background.resize((241,241))
        my_image.paste(background, (0,0), background)
        
        my_draw.rectangle(tuple(my_Car.position),outline=my_Car.outline, fill=(0, 0, 0))
        my_Car.appearance = my_Car.appearance.resize((50,50))
        pasteCarPos = (
            int((my_Car.position[2] + my_Car.position[0]) / 2)-25,
            int((my_Car.position[3] + my_Car.position[1]) / 2)-25
        )
        my_image.paste(my_Car.appearance,pasteCarPos,my_Car.appearance)
        
        my_draw.ellipse(tuple(obstacle.position),fill=(255, 255, 255, 100))
        obstacle.appearance = obstacle.appearance.resize((40,40))
        my_image.paste(obstacle.appearance, (10,190), obstacle.appearance)

        my_draw.ellipse(tuple(flag.position),fill=(255, 255, 255, 100))
        flag.appearance = flag.appearance.resize((40,40))
        my_image.paste(flag.appearance, (200,0), flag.appearance)

        '''
        #----------------------------------------------------------
        #                          Handle
        my_draw.ellipse(tuple(my_Handle.position), fill=(255, 255, 255, 100))
        my_Handle.appearance = my_Handle.appearance.resize((40,40))
        pasteHandlePos = (
            int((my_Handle.position[2] + my_Handle.position[0]) / 2) - 20,
            int((my_Handle.position[3] + my_Handle.position[1]) / 2) - 20
        )
        my_image.paste(my_Handle.appearance, pasteHandlePos, my_Handle.appearance)
        #----------------------------------------------------------
        '''
        joystick.disp.image(my_image)
        
        

if __name__ == '__main__':
    joystick = Joystick()
    background = Background()
    main(joystick,background)