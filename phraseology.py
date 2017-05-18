#!/usr/bin/env python
import pymongo
from flask import Flask, render_template, json, g
from pymongo import MongoClient

DEBUG = True
SECRET_KEY = '$(secret_key)'

# Database configuration
client = MongoClient()
db = client.phraseologydb
lessons = db.phraseologycoll
#for post in lessons.find({"type":"foot"}):
#    pprint.pprint(lesson)

app = Flask(__name__)
app.config.from_object(__name__)

def findFinalSquad(lesson):
    finalSquad = len(lesson["squads"])

def slugifyUrl(url):
    url = ' '.join(url.split('-'))
    return url

def unSlugifyUrl(url):
    url = '-'.join(url.split(' '))
    return url

@app.route('/')
def index():
    return render_template('index.html', drill=lessons.find())

@app.route('/lessons/create/')
def create():
    return render_template('create.html')

@app.route('/lessons/<lesson>')
def retrieve(lesson):
    drill = lessons.find_one({"lesson":slugifyUrl(lesson)})
    return render_template('lesson.html', drill=drill, finalSquad=findFinalSquad(drill))

@app.route('/lessons/update/')
def update():
    return render_template('create.html')


if __name__ == '__main__':
    app.run()
