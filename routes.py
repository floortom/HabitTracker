import datetime
import uuid
from flask import Blueprint, current_app, render_template, request, redirect, url_for

pages = Blueprint("habits", __name__, template_folder="templates", static_folder="static")


def today_at_midnight():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day)


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
        selectedDate = datetime.datetime.fromisoformat(dateStr)
    else:
        selectedDate = today_at_midnight()

    habitsOnDate = current_app.db.habits.find({"added": {"$lte": selectedDate}})

    completions = [habit["habit"] for habit in current_app.db.completions.find({"date": selectedDate})]

    return render_template("index.html",
                           title="Habit Tracker - Home",
                           habits=habitsOnDate,
                           selectedDate=selectedDate,
                           completions=completions
                           )


@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    today = today_at_midnight()

    if request.form:
        current_app.db.habits.insert_one(
            {"_id": uuid.uuid4().hex,
             "added": today,
             "name": request.form.get("habit"),
             }
        )
    return render_template("addHabit.html",
                           title="Habit Tracker - Add Habit",
                           selectedDate=today
                           )

@pages.post("/complete")
def complete():
    dateString = request.form.get("date")
    habit = request.form.get("habitId")
    date = datetime.datetime.fromisoformat(dateString)
    current_app.db.completions.insert_one({"date": date,
                                           "habit": habit,
                                           })

    return redirect(url_for(".index", date=dateString))
