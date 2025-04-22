from turtle import Turtle, Screen

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

screen.exitonclick()
