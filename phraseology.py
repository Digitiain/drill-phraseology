#!/usr/bin/env python
import sqlite3
from flask import Flask, render_template, json, g

DEBUG = True
SECRET_KEY = '$(secret_key)'
#DATABASE = 'database.db'

app = Flask(__name__)
app.config.from_object(__name__)

lessons = {
    "lesson":"right turn at the halt",
    "type":"foot",
    "reason":"move through 90 degrees to the right",
    "command":"Turning at the halt, RIGHT - TURN",
    "timings":"ONE - TWO, THREE - ONE",
    "squads": [
        {"command":"Turning by numbers, RIGHT TURN - ONE",
        "timings":"ONE",
        "immediately":"I forced my body through 90 degrees to the right by pivoting on the heel of my right foot and the ball of my left",
        "points":"right foot is flat on the floor, right heel is slightly raised. The rest of the body is erect AND square to the front",
        "position":"attention",
        "fall_in":"centre"},
        {"command":"SQUAD TWO",
        "timings":"TWO",
        "immediately":"I brought my left leg up in front of me until my thigh was parallel with the ground with my foot hanging naturally from the knee. I then forced my left foot in next to my right foot",
        "points":"I have returned to the correct position of attention",
        "position":"squad one",
        "fall_in":"centre"}
    ],
    "next_lesson":"left turn at the halt"
}

@app.route('/')
def index():
	#lessons = open(os.path.join(static, "data", "right_turn.json"), "r")
    return render_template('index.html',  drill=lessons)


if __name__ == '__main__':
    app.run()
