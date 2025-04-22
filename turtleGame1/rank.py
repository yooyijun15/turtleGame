import os
import datetime
from turtle import Turtle

RANKING_FILE = "rank.txt"

# 파일 생성(없을 시) 및 이름,점수,현재시각 추가
def save_rank(name, score):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RANKING_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name},{score},{current_time}\n")

# 상위 10개 랭킹 불러오기
def load_rank():
    # 점수 없을 경우
    # if not os.path.exists(RANKING_FILE):
    #     return []

    # 전체 파일 불러오기
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 분류
    records = []
    for line in lines:
        try:
            name, score, date = line.strip().split(",")
            # 리스트(records)에 튜플(name, score, date) 자료형으로 저장
            records.append((name, int(score), date))
        except ValueError:
            continue
    # score 기준 내림차순 정렬 및 상위 10개 값 반환
    return sorted(records, key=lambda x: x[1], reverse=True)[:10]

# 랭킹 화면 출력
def draw_rank(screen):
    screen.clear()
    pen = Turtle()
    pen.hideturtle()
    pen.color("black")
    pen.penup()
    pen.goto(0, 200)
    pen.write("🏆 상위 랭킹 🏆", align="center", font=("Arial", 18, "bold"))

    rankings = load_rank()
    for i, (name, score, date) in enumerate(rankings):
        pen.goto(0, 160 - i * 30)
        pen.write(f"{i+1}. {name} - {score}점", align="center", font=("Arial", 14, "normal"))

    pen.goto(0, -220)
    pen.write("화면을 클릭하면 종료됩니다.", align="center", font=("Arial", 12, "italic"))
    screen.update()
    screen.exitonclick()
