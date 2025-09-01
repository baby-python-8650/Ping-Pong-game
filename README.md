# 🏓 Pong Game

A simple Pong Game built using Python’s **Turtle graphics** module. The game features two paddles, a bouncing ball, a scoreboard, and classic Pong gameplay mechanics.  

---

## 📌 Features
- Two-player mode (Left player uses **W / S**, Right player uses **Up / Down** keys).
- Ball bounces off the top and bottom walls.
- Ball bounces off paddles with updated direction.
- Scoreboard to keep track of points.
- Game ends when the ball crosses the left or right boundary.

---

## 🛠️ Technologies Used
- **Python**
- **Turtle module** for graphics
- **Time module** for smooth ball movement
- **Custom classes**:
  - `Paddle` → For paddle movement
  - `Ball` → For ball movement and bouncing logic
  - `ScoreCard` → For tracking scores and displaying game over

---

## 🎮 How to Play
1. Clone this repository or download the code files.  
2. Make sure you have **Python 3.x** installed.  
3. Run the game:  
   ```bash
   python main.py
---
## 🎮 Controls

- **Left Paddle** → `W` (up), `S` (down)  
- **Right Paddle** → `↑` (up), `↓` (down)  

👉 Try to hit the ball with your paddle. If you miss, the opponent scores a point.  
👉 Game ends when the ball goes out of bounds.  

---

## 🚀 Future Improvements

- Add difficulty levels (increase ball speed gradually).  
- Add sound effects for paddle hit, wall bounce, and scoring.  
- Display winner when game ends.  
- Single-player mode with AI-controlled paddle.  
