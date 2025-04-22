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

# Step 2. 플레이어 생성 및 설정
player = Turtle()
player.shape("turtle")
player.color("white")
player.penup()
# 심화. 이동 후 화면 수동 업데이트
screen.update()

# Step 12-1. 여러 마리의 공격자 생성
attackers = []
attacker_num = 2
def create_attackers(num):
    for _ in range(num):
        attacker = Turtle()
        attacker.shape("turtle")
        attacker.color("red")
        attacker.penup()
        attacker.goto(random.randint(-200, 200), random.randint(-200, 200))
        attacker.showturtle()
        attackers.append(attacker)
create_attackers(attacker_num)

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
pen.write(f"⫸ 점수 : {score} ⫷", align="center", font=("Arial", 16, "bold"))

# Step 5-1. 종료 안내 표시
off = Turtle()
off.color("white")
off.penup()
off.hideturtle()
off.goto(0, -210)
off.write("z를 누르면 게임이 종료됩니다.", align="center", font=("Arial", 16, "bold"))

# Step 8-1. 여러 개의 코인 생성
coins = []
coin_num = 5

# Step 9-3. 획득한 코인 개수 변수 선언
eaten_count = 0

# Step 9-1. 여러 개의 코인 생성 함수
def create_coins(num):    
    for _ in range(num):
        coin = Turtle()
        coin.shape("circle")
        coin.color("gold")
        coin.penup()
        coin.shapesize(0.8)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        coin.goto(x, y)  
        coins.append(coin)
create_coins(coin_num)

# Step 10-3. 게임 종료
exit_game = True
def end_game(message):
    global exit_game
    exit_game = False
    player.hideturtle()
    # Step 8-3. 여러 개의 코인 화면에서 지우기
    for coin in coins:
        coin.hideturtle()
    # Step 12-4. 여러 마리의 적군 화면에서 지우기
    for attacker in attackers:
        attacker.hideturtle()
    pen.clear()
    off.clear()
    pen.goto(0, 0)
    # 10-4. 메시지 받기
    pen.write(message, align="center", font=("Arial", 20, "bold"))
    pen.goto(0, -20)
    pen.write(f"최종 점수 : {score}", align="center", font=("Arial", 14, "bold"))
    screen.update()
    time.sleep(1)
    screen.bye()

# Step 5-2. z 클릭 시 게임 종료
exit_game = True
def exit_on_z():
    end_game("👋 게임 종료 👋")

screen.onkeypress(exit_on_z, "z")

# Step 12-2. 적군 이동 및 공격
def move_attackers():
    for attacker in attackers:
        # Step 11-2. 공격자 -> 플레이어 이동
        attacker.setheading(attacker.towards(player))
        attacker.forward(2)
        # Step 11-3. 공격 감지
        if attacker.distance(player) < 20:
            end_game("💥 Game Over 💥")

speed = 0.02
# Step 10-1. 메인 루프
while exit_game:
    # Step 12-3. 적군 함수 불러오기
    move_attackers()
    # Step 10-2. check_collision() 함수 삭제
    # Step 8-2. 여러 개의 코인 감지
    for coin in coins:
        if player.distance(coin) < 20:    
            score += 1
            eaten_count += 1
            pen.clear()
            pen.write(f"⫸ 점수 : {score} ⫷", align="center", font=("Arial", 16, "bold"))
            # Step 9-2. 화면에서 코인 지우기 및 리스트에서 삭제
            coin.hideturtle()
            coins.remove(coin)
    # Step 9-4. 획득한 코인 개수와 전체 코인 개수 비교, 같을 시 코인 재배치
    if eaten_count == coin_num:
        eaten_count = 0
        create_coins(coin_num)
    # Step 5-3. 화면 업데이트
    screen.update()
    # Step 11-4. 적군 속도 제어
    time.sleep(speed)
