import datetime
from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, url_for

pages = Blueprint("habits", __name__, template_folder="templates", static_folder="static")
habits = ["Test habit"]
completions = defaultdict(list)

@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(diff) for diff in range(-3, 4)]
        return dates
    return {"dateRange": date_range}

@pages.route("/")
def index():
    dateStr = request.args.get("date")
    if dateStr:
        selectedDate = datetime.date.fromisoformat(dateStr)
    else:
        selectedDate = datetime.date.today()
    return render_template("index.html",
                           title="Habit Tracker - Home",
                           habits=habits,
                           selectedDate=selectedDate,
                           completions=completions[selectedDate]
                           )


@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    return render_template("addHabit.html",
                           title="Habit Tracker - Add Habit",
                           selectedDate=datetime.date.today()
                           )

@pages.post("/complete")
def complete():
    dateString = request.form.get("date")
    habit = request.form.get("habitName")
    date = datetime.date.fromisoformat(dateString)
    completions[date].append(habit)

    return redirect(url_for(".index", date=dateString))
