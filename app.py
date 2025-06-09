from flask import Flask, render_template, request

app = Flask(__name__)
habits = ["Test habit", "Test habit2"]

@app.route("/")
def index():
    return render_template("index.html",
                           title="Habit Tracker - Home",
                           habits=habits
                           )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    return render_template("addHabit.html", title="Habit Tracker - Add Habit")
