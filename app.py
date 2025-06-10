import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
habits = []

@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(diff) for diff in range(-3, 4)]
        return dates
    return {"dateRange": date_range}

@app.route("/")
def index():
    dateStr = request.args.get("date")
    if dateStr:
        selectedDate = datetime.date.fromisoformat(dateStr)
    else:
        selectedDate = datetime.date.today()
    return render_template("index.html",
                           title="Habit Tracker - Home",
                           habits=habits,
                           selectedDate=selectedDate
                           )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    return render_template("addHabit.html",
                           title="Habit Tracker - Add Habit",
                           selectedDate=datetime.date.today()
                           )
