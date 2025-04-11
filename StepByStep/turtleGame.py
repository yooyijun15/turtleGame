from turtle import Turtle, Screen
from random import randint
import time

class turtleGame():
    def __init__(self):
        # 화면
        self.screen = Screen()
        self.screen.title("거북이🐢 게임")
        self.screen.bgcolor("black")
        self.screen.setup(width=500, height=500)
        self.screen.tracer(0)

        # 플레이어
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("white")
        self.player.penup()
        self.player.goto(0, -200)
        self.screen.update()
        
        # UI
        self.pen = Turtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 220)

        # 변수 선언
        self.round_number = 1
        self.lives = 3
        self.score = 0
        self.target_circle = 10
        self.total_rounds = 5
        self.round_time = 30

        self.setup_controls()
        
    # 키보드 이벤트    
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        
    # 좌/우 이동
    def move_left(self):
        x = self.player.xcor() - 20
        if x > -240:
            self.player.setx(x)
            self.player.setheading(180)
            self.screen.update()
            
    def move_right(self):
        x = self.player.xcor() + 20
        if x < 240:
            self.player.setx(x)
            self.player.setheading(0)
            self.screen.update()
        
    # 생명 표시
    def get_heart_display(self):
        return "♥" * self.lives + "♡" * (3 - self.lives)

    # 아이템
    def create_items(self, shape, color, count):
        items = []
        for _ in range(count):
            item = Turtle()
            item.shape(shape)
            item.color(color)
            item.penup()
            item.speed(0)
            x = randint(-250, 250)
            y = randint(230, 250)
            item.goto(x, y)
            items.append(item)
        return items

    # 라운드
    def play_round(self):
        start_time = time.time()
        self.score = 0

        # 난이도 
        speed = self.round_number + 2
        enemy_number = self.round_number + 3
        score_number = self.round_number + 4
        goal_circle = self.target_circle + (self.round_number-1)*5

        # 아이템 생성
        enemy_triangles = self.create_items("triangle", "red", enemy_number)
        enemy_squares = self.create_items("square", "blue", enemy_number)
        score_circle = self.create_items("circle", "green", score_number)

        # 게임 진행
        game_over = True
        while game_over:
            # 시간
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(0, round(self.round_time - elapsed_time)) 

            # 아이템
            for item in enemy_triangles+enemy_squares:
                y = item.ycor() - speed
                item.sety(y)
                if y < -250:
                    item.goto(randint(-250, 250), randint(230, 250))
                if self.player.distance(item) < 20:
                    self.lives -= 1
                    item.goto(randint(-250, 250), randint(230, 250))
            for item in score_circle:
                y = item.ycor() - speed
                item.sety(y)
                if y < -250:
                    item.goto(randint(-250, 250), randint(230, 250))
                if self.player.distance(item) < 20:
                    self.score += 1
                    item.goto(randint(-250, 250), randint(230, 250))

            # UI
            self.pen.clear()
            self.pen.write(
                f" ⫸ ROUND {self.round_number} ⫷         ⏱ {remaining_time}초     생명 : {self.get_heart_display()}        {self.score} / {goal_circle}",
                align="center", font=("Arial", 16, "bold")
            )
            self.screen.update()

            # 라운드 종료
            if self.lives <= 0 or elapsed_time >= self.round_time or self.score >= goal_circle:
                game_over = False
               
        time.sleep(0.02)
        
        # 아이템 삭제
        for item in enemy_triangles+enemy_squares+score_circle:
            item.hideturtle()
            item.clear()
            del item
            
        # 게임 종료
        if self.lives <= 0 or self.score < self.target_circle:
            self.pen.goto(0, 0) 
            self.pen.write(f"💀 Game Over 💀", align="center", font=("Arial", 24, "bold"))
            self.screen.update()
            # 재도전 팝업
            time.sleep(1)
            retry = self.screen.textinput("재도전", "재도전 하시겠습니까? (yes/no)")
            if retry.lower() == "yes":
                self.lives = 3
                self.score = 0
                self.pen.goto(0, 220)
                self.setup_controls()
                self.round_number -= 1
                return True
            return False
        return True

    # 게임 실행      
    def run(self):
        while self.round_number <= self.total_rounds:
            result = self.play_round()
            if not result:
                break
            self.round_number += 1
        
# 실행
if __name__ == "__main__":
    game = turtleGame()
    game.run()
