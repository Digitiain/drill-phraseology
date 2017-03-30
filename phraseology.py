#!/usr/bin/env python
from flask import Flask, render_template, json

DEBUG = True
SECRET_KEY = '$(secret_key)'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	lessons = open(os.path.join(static, "data", "right_turn.json"), "r")
    return render_template('index.html',  lessons=lessons)


if __name__ == '__main__':
    app.run()