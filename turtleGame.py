from turtle import Turtle, Screen
from random import randint
import time

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
target_circle = 10

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

# Step 7. 아이템 객체 생성 및 설정
# Step 7-1. 아이템 생성 함수 정의
def create_items(shape, color, count):
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

# Step 6. 게임 루프 생성
# Step 6-1. 변수 선언
total_rounds = 5
round_time = 30

# Step 6-2. 라운드 루프 시작
while round_number <= total_rounds:
    start_time = time.time()
    # .time() : 현재 시간을 초 단위로 반환
    game_over = True

    # Step 9. 난이도 조정
    # Step 9-1. 변수 선언
    speed = round_number + 2
    enemy_number = round_number + 3
    score_number = round_number + 4
    goal_circle = target_circle + (round_number-1)*5

    # Step 7-2. 아이템 객체 생성
    # Step 9-2. 변수로 변경
    enemy_triangles = create_items("triangle", "red", enemy_number)
    enemy_squares = create_items("square", "blue", enemy_number)
    score_circle = create_items("circle", "green", score_number)


    while game_over:
        current_time = time.time()
        elapsed_time = current_time - start_time # 현재 시간 - 시작 시간 = 경과 시간
        remaining_time = max(0, round(round_time - elapsed_time)) # 남은 시간, round() 함수 사용하여 소수점 보정

        # Step 7-3. 아이템 객체 아래로 떨어트리기
        for item in enemy_triangles+enemy_squares:
            # Step 9-2. 변수로 변경
            y = item.ycor() - speed # 숫자 클수록 속도 UP
            item.sety(y)
            # 바닥에 닿으면 랜덤 시작 위치로 이동
            if y < -250:
                item.goto(randint(-250, 250), randint(230, 250))
            # 플레이어에 닿으면 1) 생명 하나 없애고, 2) 랜덤 시작 위치로 이동
            if player.distance(item) < 20:
                lives -= 1
                item.goto(randint(-250, 250), randint(230, 250))
        for item in score_circle:
            y = item.ycor() - speed
            item.sety(y)
            if y < -250:
                item.goto(randint(-250, 250), randint(230, 250))
            if player.distance(item) < 20:
                score += 1
                item.goto(randint(-250, 250), randint(230, 250))

        # Step 5-3. 화면 정보 출력
        pen.clear()
        # Step 9-2. 변수로 변경
        pen.write(
            f" ⫸ ROUND {round_number} ⫷         ⏱ {remaining_time}초     생명 : {get_heart_display(lives)}        {score} / {goal_circle}",
            align="center", font=("Arial", 16, "bold")
        )
        # Step 6-3. 화면 수동 업데이트
        screen.update()

        # Step 8. 게임 종료 (생명 소진)
        # Step 8-1. 하위 루프 종료
        if lives <= 0:
            game_over = False
            
        # Step 6-4. 지정된 시간 경과 시, 루프 종료(해당 라운드 종료)
        if elapsed_time >= round_time:
            game_over = False

        # Step 10. 목표 점수 도달 시, 루프 종료(해당 라운드 종료)
        if score >= goal_circle:
            game_over = False
            
    time.sleep(0.02)
    # .sleep(초) : 일시정지
    
    # Step 7-4. 해당 라운드에서 생성된 아이템 객체 삭제
    for item in enemy_triangles+enemy_squares+score_circle:
        item.hideturtle()
        item.clear()
        del item # 메모리 정리
        
    # Step 8-2. 상위 루프 종료 및 Game Over 문구 표시 (생명 소진 or 점수 부족)
    if lives <= 0 or score < target_circle:
        pen.goto(0, 0) 
        pen.write(f"💀 Game Over 💀", align="center", font=("Arial", 24, "bold"))
        screen.update()
        # Step 11. 재도전 팝업
        time.sleep(1)
        retry = screen.textinput("재도전", "재도전 하시겠습니까? (yes/no)")
        if retry.lower() == "yes":
            lives = 3
            score = 0
            pen.goto(0, 220)
            # .textinput() 실행 시, 하위 내용 다시 호출해야한다.
            screen.listen()
            screen.onkeypress(move_left, "Left")
            screen.onkeypress(move_right, "Right")
            continue
        else:
            break
               
    # Step 6-5. 다음 라운드 이동
    round_number += 1

    # Step 7-5. 점수 초기화
    score = 0
         
# Step 1-2. 화면 클릭 시 종료
screen.exitonclick()
