import sqlite3
import datetime
from turtle import Turtle

DB_NAME = "rank.db"

# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS rankings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# 랭킹 저장
def save_rank(name, score):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO rankings (name, score, date) VALUES (?, ?, ?)", (name, score, current_time))
    conn.commit()
    conn.close()

# 랭킹 로드
def load_rank(limit=10):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, score, date FROM rankings ORDER BY score DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

# 랭킹 그리기
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

# (터미널) sqlite3 - 데이터베이스 확인 방법
# sqlite3 rank.db
# > SELECT * FROM rankings;
# .quit
