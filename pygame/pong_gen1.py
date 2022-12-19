import pygame as pg
pg.init()

class Paddle():
    def __init__(self, x, y, width, height):
        pg.init()
        self.x = x
        self.y = y 
        self.pad_width = width
        self.pad_height = height
        self.pad_color = (255,255,255)
        self.pad_velocity = 4

    def draw(self, screen):
        pg.draw.rect(screen, self.pad_color, (self.x, self.y, self.pad_width, self.pad_height))

    def move(self, up=True):
        if up:
            self.y -= self.pad_velocity
        else:
            self.y += self.pad_velocity 

    def paddle_bind(self, keys, player):
        if player == "left":
            if keys[pg.K_w] and self.y - self.pad_velocity >= 0:
                self.move(up=True)
            if keys[pg.K_s] and self.y + self.pad_velocity + self.pad_height <= Pong().screen_height:
                self.move(up=False)
        if player == "right":
            if keys[pg.K_UP] and self.y - self.pad_velocity >= 0:
                self.move(up=True)
            if keys[pg.K_DOWN] and self.y + self.pad_velocity + self.pad_height <= Pong().screen_height:
                self.move(up=False)
        
        

class Ball():
    pass

class Score():
    pass

class Pong():
    def __init__(self):
        pg.init()
        self.screen_width = 900
        self.screen_height = 700
        self.backround_color = (0,0,0)
        self.fps = 60
        self.pad_height = 100
        self.pad_width = 20

    def draw(self, screen, paddles):
        screen.fill(self.backround_color)

        for paddle in paddles:
            paddle.draw(screen)
        
        pg.display.update()

    def run_game(self):
        screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Pong")
        run = True
        clock = pg.time.Clock()

        left_paddle = Paddle(10, self.screen_height//2 - self.pad_height//2, self.pad_width, self.pad_height)
        right_paddle = Paddle(self.screen_width - 10 - self.pad_width, self.screen_height//2 - self.pad_height//2, self.pad_width, self.pad_height)

        while run:
            clock.tick(self.fps)
            self.draw(screen, [left_paddle, right_paddle])

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    run = False
                    break
        
            keys = pg.key.get_pressed()
            left_paddle.paddle_bind(keys, player="left")
            right_paddle.paddle_bind(keys, player="right")

        pg.quit()

if __name__=="__main__":
    pong = Pong()
    pong.run_game()