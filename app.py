from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

FILE = "attendance.csv"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    roll = request.form["roll"]
    status = request.form["status"]
    import os

    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        df = pd.read_csv(FILE)
    else:
        df = pd.DataFrame(columns=["name","roll","status"])

    df.loc[len(df)] = [name, roll, status]
    df.to_csv(FILE, index=False)

    return redirect("/view")

@app.route("/view")
def view():
    if os.path.exists(FILE):
        df = pd.read_csv(FILE)
        return df.to_html()
    else:
        return "No data yet"

app.run(debug=True)


@app.route("/view")
def view():
    df = pd.read_csv(FILE)
    data = df.to_dict(orient="records")
    return render_template("view.html", data=data)


if __name__ == "__main__":
    app.run()
