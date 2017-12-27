from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash


app=Flask(__name__)

db = SQL("sqlite:///users.db")


@app.route("/")
def index():

    return render_template("login.html")

@app.route("/login",methods=["GET","POST"])
def login():


    if request.method=="POST":

        if not request.form.get("username"):
            return render_template("apology.html")

        elif not request.form.get("password"):
            return render_template("apology.html")


        rows=db.execute("SELECT *FROM users WHERE username=:username",username=request.form.get("username"))
        if not rows:
            return render_template("notregister.html")

        if request.form.get("password") != rows[0]["password"]:
            return render_template("passinc.html")

        return render_template("sucess.html")

    else:
        return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        if not request.form.get("username"):
            return render_template("apology.html")

        elif not request.form.get("password"):
            return render_template("apology.html")

        elif request.form.get("password")!=request.form.get("confirmpassword"):
            return render_template("passmatch.html")


        result=db.execute("INSERT INTO users(username,password) VALUES(:username,:password)",username=request.form.get("username"),password=request.form.get("password"))

        return render_template("registered.html")

    else:
        return render_template("register.html")


