from flask import Flask, flash, request, render_template, flash
app = Flask(__name__)
@app.route('/rk')
def iram():
    return render_template("index.html")