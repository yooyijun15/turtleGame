from turtle import Turtle, Screen
from random import randint
import time
from config import SCREEN_WIDTH, SCREEN_HEIGHT, INIT_LIVES, ROUND_TIME, TOTAL_ROUNDS, TARGET_BASE
from rank_db import init_db, save_rank, draw_rank
#from rank import save_rank, draw_rank
#import pygame

class turtleGame:
    def __init__(self):
        #pygame.mixer.init()
        #self.bgm = pygame.mixer.Sound("bgm.wav")
        #self.bgm.set_volume(0.3)

        self.screen = Screen()
        self.screen.title("거북이🐢 게임")
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("white")
        self.player.penup()
        self.player.goto(0, -200)
        self.screen.update()

        self.pen = Turtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 220)

        self.round_number = 1
        self.lives = INIT_LIVES
        self.score = 0
        self.total_score = 0
        self.target_circle = TARGET_BASE
        self.total_rounds = TOTAL_ROUNDS
        self.round_time = ROUND_TIME

        self.setup_controls()
        #self.bgm.play(-1)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

    def move_left(self):
        x = self.player.xcor() - 20
        if x > -SCREEN_WIDTH // 2 + 10:
            self.player.setx(x)
            self.player.setheading(180)
            self.screen.update()

    def move_right(self):
        x = self.player.xcor() + 20
        if x < SCREEN_WIDTH // 2 - 10:
            self.player.setx(x)
            self.player.setheading(0)
            self.screen.update()

    def get_heart_display(self):
        return "♥" * self.lives + "♡" * (3 - self.lives)

    def create_items(self, shape, color, count):
        items = []
        for _ in range(count):
            item = Turtle()
            item.shape(shape)
            item.color(color)
            item.penup()
            item.speed(0)
            x = randint(-240, 240)
            y = randint(230, 250)
            item.goto(x, y)
            items.append(item)
        return items

    def play_round(self):
        start_time = time.time()
        self.score = 0

        speed = self.round_number + 2
        enemy_number = self.round_number + 3
        score_number = self.round_number + 4
        goal_circle = self.target_circle + (self.round_number - 1) * 5

        enemy_triangles = self.create_items("triangle", "red", enemy_number)
        enemy_squares = self.create_items("square", "blue", enemy_number)
        score_circle = self.create_items("circle", "green", score_number)

        game_over = True
        while game_over:
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(0, round(self.round_time - elapsed_time))

            for item in enemy_triangles + enemy_squares:
                y = item.ycor() - speed
                item.sety(y)
                if y < -250:
                    item.goto(randint(-240, 240), randint(230, 250))
                if self.player.distance(item) < 20:
                    self.lives -= 1
                    item.goto(randint(-240, 240), randint(230, 250))

            for item in score_circle:
                y = item.ycor() - speed
                item.sety(y)
                if y < -250:
                    item.goto(randint(-240, 240), randint(230, 250))
                if self.player.distance(item) < 20:
                    self.score += 1
                    item.goto(randint(-240, 240), randint(230, 250))

            self.pen.clear()
            self.pen.write(
                f" ⫸ ROUND {self.round_number} ⫷    ⏱ {remaining_time}초    생명 : {self.get_heart_display()}     ⭐ {self.total_score}     {self.score} / {goal_circle}",
                align="center", font=("Arial", 16, "bold")
            )
            self.screen.update()

            if self.lives <= 0 or elapsed_time >= self.round_time:
                game_over = False

            if self.score >= goal_circle:
                self.total_score += remaining_time * self.round_number
                game_over = False

        time.sleep(0.02)

        for item in enemy_triangles + enemy_squares + score_circle:
            item.hideturtle()
            item.clear()
            del item

        if self.lives <= 0 or self.score < self.target_circle:
            self.pen.goto(0, 0)
            self.pen.write("💀 Game Over 💀", align="center", font=("Arial", 24, "bold"))
            self.screen.update()
            time.sleep(1)
            retry = self.screen.textinput("재도전", "재도전 하시겠습니까? (yes/no)")
            if retry and retry.lower() == "yes":
                self.lives = INIT_LIVES
                self.score = 0
                self.total_score -= 3 * (self.round_number - 1)
                self.pen.goto(0, 220)
                self.setup_controls()
                self.round_number -= 1
                return True
            return False

        return True

    def run(self):
        while self.round_number <= self.total_rounds:
            result = self.play_round()
            if not result:
                break
            self.round_number += 1

        # 랭킹
        name = self.screen.textinput("점수 기록", f"최종 점수: {self.total_score}점\n이름을 입력하세요:")
        if name:
            save_rank(name, self.total_score)
            draw_rank(self.screen)

init_db()
