from turtle import Turtle, Screen
import random
import time

# Step 1. 화면 생성 및 설정
screen = Screen()
screen.title("거북이🐢 게임")
screen.bgcolor("black")
screen.setup(width=500, height=500)
# 심화. 자동 애니메이션 OFF
screen.tracer(0)

# Step 2. 거북이 생성 및 설정
player = Turtle()
player.shape("turtle")
player.color("white")
player.penup()
# 심화. 이동 후 화면 수동 업데이트
screen.update()

# Step 3-1. 플레이어 상/하/좌/우 움직이기
def move_left():
    # .xcor() : 플레이어의 현재 x좌표 가져오는 함수
    x = player.xcor() - 20
    # 벽 충돌 방지 조건
    if x > -240:
      # .setx(숫자) : x좌표 ()안의 값으로 변경하는 함수
      player.setx(x)
      # .setheading(각도) : 플레이어 방향 변경하는 함수
      player.setheading(180)
      # 심화. 이동 후 화면 수동 업데이트
      screen.update()

def move_right():
    x = player.xcor() + 20
    if x < 240:
        player.setx(x)
        player.setheading(0)
        screen.update()

def move_up():
    y = player.ycor() + 20
    if y < 240:  
        player.sety(y)
        player.setheading(90)
        screen.update()

def move_down():
    y = player.ycor() - 20
    if y > -240:
        player.sety(y)
        player.setheading(270)
        screen.update()
    
# Step 3-2. 키보드 이벤트 연결
screen.listen()
# .onkeypress(실행할 함수명, "방향키")        
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Step 4. 점수 표시
score = 0
pen = Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)

pen.write(f"⫸ 점수 :  {score} ⫷", align="center", font=("Arial", 16, "bold"))

# Step 5-1. 종료 안내 표시
off = Turtle()
off.color("white")
off.penup()
off.hideturtle()
off.goto(0, -210)
off.write("z를 누르면 게임이 종료됩니다.", align="center", font=("Arial", 16, "bold"))

# Step 6-1. 코인 한개 생성
coin = Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.shapesize(0.8)

def random_coin(): 
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    coin.goto(x, y)
    
random_coin()

# Step 7-1. 점수 획득
def check_collision():
    global score
    if player.distance(coin) < 20:
        score += 1
        pen.clear()
        pen.write(f"⫸ 점수 :  {score} ⫷", align="center", font=("Arial", 16, "bold"))
        random_coin()

# Step 5-2. z 클릭 시 게임 종료
exit_game = True
def exit_on_z():
    global exit_game
    exit_game = False
    player.hideturtle()
    # Step 6-2. 코인 화면에서 지우기
    coin.hideturtle()
    pen.clear()
    off.clear()
    pen.goto(0, 0)
    pen.write("👋 게임 종료 👋", align="center", font=("Arial", 20, "bold"))
    pen.goto(0, -20)
    pen.write(f"최종 점수 : {score}", align="center", font=("Arial", 14, "bold"))
    screen.update()
    time.sleep(1)
    screen.bye()

screen.onkeypress(exit_on_z, "z")

# Step 5-3. 화면 업데이트
while exit_game:
    # Step 7-2. 점수 획득 함수 불러오기
    check_collision()
    screen.update()
