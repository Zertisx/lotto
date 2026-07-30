from flask import Flask, render_template, request
from Lotto import get_winning_numbers, calculate_prize
from database import save_play, setup_database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("play.html")

@app.route("/play", methods=["POST"])
def play():
    username = request.form["username"]
    numbers = [int(request.form[f"n{i}"]) for i in range(1, 7)]
    winning = get_winning_numbers()
    prize = calculate_prize(numbers, winning)
    save_play(username, numbers, winning, prize)
    return render_template("result.html", numbers=numbers, winning=winning, prize=prize)

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)