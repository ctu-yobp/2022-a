import pygame as pg
from pong_gen1 import *

class Pong2(Pong):

    def __init__(self):
        super().__init__()

    def collision_sound(self):
        sound = pg.mixer.Sound("crash.wav")
        sound.play()

    def collision_sound2(self):
        sound = pg.mixer.Sound("crash2.wav")
        sound.play()

    def collision_edge(self, ball):
        if ball.y + ball.radius >= self.screen_height:
            self.collision_sound2()
        elif ball.y - ball.radius <= 0:
            self.collision_sound2()
        return super().collision_edge(ball)

    def collision_lpaddle(self, ball, left_paddle):
        if ball.dx < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.pad_height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.pad_width:
                    self.collision_sound()
        return super().collision_lpaddle(ball, left_paddle) # je to vyhodne ??

    def collision_rpaddle(self, ball, right_paddle):
        if ball.dx > 0:    
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.pad_height:
                if ball.x + ball.radius >= right_paddle.x:
                    self.collision_sound()
        return super().collision_rpaddle(ball, right_paddle) # je to vyhodne ??

if __name__=="__main__":
    pong = Pong2()
    pong.run_game()