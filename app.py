import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///website_menu.db")

@app.route("/", methods=["GET", "POST"])
def index():
    print("Website loaded.")
    if request.method == "POST":
        return redirect("/")

    else:
        return render_template("index.html")