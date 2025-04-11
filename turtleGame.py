from turtle import Turtle, Screen

# Step 1. 화면 설정
# Step 1-1. 객체 생성 및 설정
screen = Screen()
screen.title("거북이🐢 게임")
screen.bgcolor("black")
screen.setup(width=500, height=500)

# Step 4. 자연스러운 애니메이션 설정
# Step 4-1. 자동 애니메이션 OFF
# .tracer(0) : 자동 애니메이션 OFF
screen.tracer(0)

# Step 2. 플레이어 객체 생성 및 설정
player = Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -200)

# Step 4-2. 초기 화면 수동 업데이트
# .update() : 화면 수동 업데이트
screen.update()

# Step 3. 플레이어 좌/우 이동시키기
# Step 3-1. 함수 정의 
def move_left():
    x = player.xcor() - 20
    # .xcor() : 플레이어의 현재 x좌표 가져오기
    # 플레이어를 왼쪽으로 20만큼 움직이기 위해 -20으로 변경한 값을 x에 저장합니다.
    if x > -240:
    # 벽 충돌 방지 조건
        player.setx(x)
        # .setx(숫자) : x좌표 ()안의 값으로 변경
        player.setheading(180)
        # .setheading(각도) : 플레이어 방향 변경
        # Step 4-3. 이동 후 화면 수동 업데이트
        screen.update()

def move_right():
    x = player.xcor() + 20
    if x < 240:
        player.setx(x)
        player.setheading(0)
        screen.update()

# Step 3-2. 키보드 이벤트 연결
screen.listen()
# .listen() : 키보드 입력 수신 대기
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
# .onkeypress(실행할 함수명, "방향키")


# Step 5. 라운드 및 생명 표시

# Step 5-1. 변수 선언
round_number = 1
lives = 3
score = 0
target_circle = 15

# Step 5-2. 라운드 및 생명 표시 객체 생성 및 설정
pen = Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)

# Step 5-4. 생명 표시 함수 정의
def get_heart_display(lives):
    full = "♥"
    empty = "♡"
    return full * lives + empty * (3 - lives)

# Step 5-3. 화면 정보 출력
pen.write(
    f" ⫸ ROUND {round_number} ⫷                           생명 : {get_heart_display(lives)}             {score} / {target_circle}",
    align="center", font=("Arial", 16, "bold")
)
