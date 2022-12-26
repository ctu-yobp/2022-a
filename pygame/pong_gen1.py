import pygame as pg

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
    def __init__(self, x, y, radius):
        pg.init()
        self.x = self.x_or = x
        self.y = self.y_or = y
        self.radius = radius
        self.ball_mvelocity = 4
        self.ball_color = (255,255,255)
        self.dx = self.ball_mvelocity
        self.dy = 0

    def draw(self, screen):
        pg.draw.circle(screen, self.ball_color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def reset(self):
        self.x = self.x_or
        self.y = self.y_or
        self.dx *= -1
        self.dy = 0


class Score():
    def __init__(self):
        self.font = pg.font.SysFont("comicsans", 50)
        self.winning_score = 10
        self.left_score = 0
        self.right_score = 0

    # def score_counter(self):
    #     if Pong().ball.x < 0:
    #         Pong().score.right_score += 1
    #         Pong().ball.reset()
    #     elif Pong().ball.x > Pong().screen_width:
    #         Pong().score.left_score += 1
    #         Pong().ball.reset()
        
class Pong():
    def __init__(self):
        pg.init()
        self.screen_width = 900
        self.screen_height = 700
        self.backround_color = (0,0,0)
        self.fps = 60
        self.pad_height = 100
        self.pad_width = 20
        self.white = (255,255,255)

        self.ball = Ball(self.screen_width//2, self.screen_height//2, 10)
        self.left_paddle = Paddle(10, self.screen_height//2 - self.pad_height//2, self.pad_width, self.pad_height)
        self.right_paddle = Paddle(self.screen_width - 10 - self.pad_width, self.screen_height//2 - self.pad_height//2, self.pad_width, self.pad_height)
        self.score = Score()
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))

    def draw(self, screen, paddles, ball, left_score, right_score):
        screen.fill(self.backround_color)

        left_score_text = Score().font.render(f"{left_score}", 1, self.white)
        right_score_text = Score().font.render(f"{right_score}", 1, self.white)
        screen.blit(left_score_text, (self.screen_width//4 - left_score_text.get_width()//2, 20))
        screen.blit(right_score_text, (self.screen_width * 0.75 - right_score_text.get_width()//2, 20))

        for paddle in paddles:
            paddle.draw(screen)
        
        ball.draw(screen)

        pg.display.update()

    def bounce_angle(self, ball, paddle):
        middle_y = paddle.y + paddle.pad_height / 2
        delta_y = middle_y - ball.y
        rf = (paddle.pad_height / 2) / ball.ball_mvelocity
        ball.dy = -1 * delta_y / rf

    def collision(self, ball, left_paddle, right_paddle):
        if ball.y + ball.radius >= self.screen_height:
            ball.dy *= -1
        elif ball.y - ball.radius <= 0:
            ball.dy *= -1

        if ball.dx < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.pad_height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.pad_width:
                    ball.dx *= -1

                    self.bounce_angle(ball, left_paddle)

        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.pad_height:
                if ball.x + ball.radius >= right_paddle.x :
                    ball.dx *= -1

                    self.bounce_angle(ball, right_paddle)

   # ###########################
   # predelat do tridy Score ???
   # ########################### 
    def score_counter(self):
        if self.ball.x < 0:
            self.score.right_score += 1
            self.ball.reset()
        elif self.ball.x > self.screen_width:
            self.score.left_score += 1
            self.ball.reset()

    def end_game(self):
        end = False
        if self.score.left_score == self.score.winning_score:
            end = True
            end_text = "left player won"
        elif self.score.right_score == self.score.winning_score:
            end = True
            end_text = "right player won"
        
        if end:
            text = self.score.font.render(end_text, 1, self.white)
            self.screen.blit(text, ((self.screen_width//2 - text.get_width()//2), self.screen_height//2) )
            pg.display.update()
            pg.time.delay(5000)
            pg.quit()
   # ###########################
   # predelat do tridy Score ???
   # ###########################

    def run_game(self):
        pg.display.set_caption("Pong")
        run = True
        clock = pg.time.Clock()

        while run:

            clock.tick(self.fps)

            self.draw(self.screen, [self.left_paddle, self.right_paddle], self.ball, self.score.left_score, self.score.right_score)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            
            keys = pg.key.get_pressed()
            self.left_paddle.paddle_bind(keys, player="left")
            self.right_paddle.paddle_bind(keys, player="right")

            self.ball.move()

            self.collision(self.ball, self.left_paddle, self.right_paddle)

            self.score_counter()

            self.end_game()

        pg.quit()

if __name__=="__main__":
    pong = Pong()
    pong.run_game()