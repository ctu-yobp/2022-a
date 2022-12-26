import pygame as pg
from pong_gen1 import *

# class Paddle(Paddle):

#     def inc_velocity(self):
#         self.pad_velocity *= 1.05


# class Ball(Ball):
#     def __init__(self):
#         super().__init__()

#     def inc_velocity(self):
#         self.dx *= 1.05

#     def change_dir(self):
#         self.dx *= -1 


class Pong2(Pong):

    def __init__(self):
        super().__init__()

    def collision_sound(self):
        sound = pg.mixer.Sound("crash.wav")
        sound.play()

    def collision_sound2(self):
        sound = pg.mixer.Sound("crash2.wav")
        sound.play()

    def collision(self, ball, left_paddle, right_paddle):
        if ball.y + ball.radius >= self.screen_height:
            ball.dy *= -1
            self.collision_sound2()
        elif ball.y - ball.radius <= 0:
            ball.dy *= -1
            self.collision_sound2()

        if ball.dx < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.pad_height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.pad_width:
                    ball.dx *= -1 
                    self.bounce_angle(ball, left_paddle)
                    self.collision_sound()
                    
        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.pad_height:
                if ball.x + ball.radius >= right_paddle.x :
                    ball.dx *= -1 
                    self.bounce_angle(ball, right_paddle)
                    self.collision_sound()

if __name__=="__main__":
    pong = Pong2()
    pong.run_game()