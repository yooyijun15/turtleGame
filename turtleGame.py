from turtle import Turtle, Screen
from random import randint
import time

class turtleGame():
    def __init__(self):
        # Step 1. 화면 설정
        # Step 1-1. 객체 생성 및 설정
        self.screen = Screen()
        self.screen.title("거북이🐢 게임")
        self.screen.bgcolor("black")
        self.screen.setup(width=500, height=500)

        # Step 4. 자연스러운 애니메이션 설정
        # Step 4-1. 자동 애니메이션 OFF
        # .tracer(0) : 자동 애니메이션 OFF
        self.screen.tracer(0)

        # Step 2. 플레이어 객체 생성 및 설정
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("white")
        self.player.penup()
        self.player.goto(0, -200)

        # Step 4-2. 초기 화면 수동 업데이트
        # .update() : 화면 수동 업데이트
        self.screen.update()

        # Step 5. 라운드 및 생명 표시
        # Step 5-1. 변수 선언
        self.round_number = 1
        self.lives = 3
        self.score = 0
        self.target_circle = 10
        
        # Step 5-2. 라운드 및 생명 표시 객체 생성 및 설정
        self.pen = Turtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 220)

        # Step 6. 게임 루프 생성
        # Step 6-1. 변수 선언
        self.total_rounds = 5
        self.round_time = 30

        self.setup_controls()
        
    def setup_controls(self):
        # Step 3-2. 키보드 이벤트 연결
        self.screen.listen()
        # .listen() : 키보드 입력 수신 대기
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        # .onkeypress(실행할 함수명, "방향키")
        
    # Step 3. 플레이어 좌/우 이동시키기
    # Step 3-1. 함수 정의 
    def move_left(self):
        x = self.player.xcor() - 20
        # .xcor() : 플레이어의 현재 x좌표 가져오기
        # 플레이어를 왼쪽으로 20만큼 움직이기 위해 -20으로 변경한 값을 x에 저장합니다.
        if x > -240:
        # 벽 충돌 방지 조건
            self.player.setx(x)
            # .setx(숫자) : x좌표 ()안의 값으로 변경
            self.player.setheading(180)
            # .setheading(각도) : 플레이어 방향 변경
            # Step 4-3. 이동 후 화면 수동 업데이트
            self.screen.update()
            
    def move_right(self):
        x = self.player.xcor() + 20
        if x < 240:
            self.player.setx(x)
            self.player.setheading(0)
            self.screen.update()
        
    # Step 5-4. 생명 표시 함수 정의
    def get_heart_display(self):
        return "♥" * self.lives + "♡" * (3 - self.lives)

    # Step 7. 아이템 객체 생성 및 설정
    # Step 7-1. 아이템 생성 함수 정의
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

    def play_round(self):
        start_time = time.time()
        # .time() : 현재 시간을 초 단위로 반환

        # Step 7-5. 점수 초기화
        self.score = 0

        # Step 9. 난이도 조정
        # Step 9-1. 변수 선언
        speed = self.round_number + 2
        enemy_number = self.round_number + 3
        score_number = self.round_number + 4
        goal_circle = self.target_circle + (self.round_number-1)*5

        # Step 7-2. 아이템 객체 생성
        # Step 9-2. 변수로 변경
        enemy_triangles = self.create_items("triangle", "red", enemy_number)
        enemy_squares = self.create_items("square", "blue", enemy_number)
        score_circle = self.create_items("circle", "green", score_number)


        game_over = True
        while game_over:
            current_time = time.time()
            elapsed_time = current_time - start_time # 현재 시간 - 시작 시간 = 경과 시간
            remaining_time = max(0, round(self.round_time - elapsed_time)) # 남은 시간, round() 함수 사용하여 소수점 보정

            # Step 7-3. 아이템 객체 아래로 떨어트리기
            for item in enemy_triangles+enemy_squares:
                # Step 9-2. 변수로 변경
                y = item.ycor() - speed # 숫자 클수록 속도 UP
                item.sety(y)
                # 바닥에 닿으면 랜덤 시작 위치로 이동
                if y < -250:
                    item.goto(randint(-250, 250), randint(230, 250))
                # 플레이어에 닿으면 1) 생명 하나 없애고, 2) 랜덤 시작 위치로 이동
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

            # Step 5-3. 화면 정보 출력
            self.pen.clear()
            # Step 9-2. 변수로 변경
            self.pen.write(
                f" ⫸ ROUND {self.round_number} ⫷         ⏱ {remaining_time}초     생명 : {self.get_heart_display()}        {self.score} / {goal_circle}",
                align="center", font=("Arial", 16, "bold")
            )
            # Step 6-3. 화면 수동 업데이트
            self.screen.update()

            # Step 8. 게임 종료 (생명 소진)
            # Step 8-1. 하위 루프 종료
            # Step 6-4. 지정된 시간 경과 시, 루프 종료(해당 라운드 종료)
            # Step 10. 목표 점수 도달 시, 루프 종료(해당 라운드 종료)
            if self.lives <= 0 or elapsed_time >= self.round_time or self.score >= goal_circle:
                game_over = False
               
        time.sleep(0.02)
        # .sleep(초) : 일시정지
        
        # Step 7-4. 해당 라운드에서 생성된 아이템 객체 삭제
        for item in enemy_triangles+enemy_squares+score_circle:
            item.hideturtle()
            item.clear()
            del item # 메모리 정리
            
        # Step 8-2. 상위 루프 종료 및 Game Over 문구 표시 (생명 소진 or 점수 부족)
        if self.lives <= 0 or self.score < self.target_circle:
            self.pen.goto(0, 0) 
            self.pen.write(f"💀 Game Over 💀", align="center", font=("Arial", 24, "bold"))
            self.screen.update()
            # Step 11. 재도전 팝업
            time.sleep(1)
            retry = self.screen.textinput("재도전", "재도전 하시겠습니까? (yes/no)")
            if retry.lower() == "yes":
                self.lives = 3
                self.score = 0
                self.pen.goto(0, 220)
                # .textinput() 실행 시, 하위 내용 다시 호출해야한다.
                self.setup_controls()
                # (추가)
                self.round_number -= 1
                return True
            return False
        return True
            
    def run(self):
        # Step 6-2. 라운드 루프 시작
        while self.round_number <= self.total_rounds:
            result = self.play_round()
            if not result:
                break
                       
            # Step 6-5. 다음 라운드 이동
            self.round_number += 1
        
# (추가) 실행
if __name__ == "__main__":
    game = turtleGame()
    game.run()



