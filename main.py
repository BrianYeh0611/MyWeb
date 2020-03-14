import os
import glob
from flask import Flask, render_template
server = Flask("Brian")

@server.route("/")
def index():
    ds = glob.glob("Jokes/*")
    ds = [d.split("/")[-1] for d in ds]
    return render_template("index.html", dirs=ds)

@server.route("/Jokes/<c>")
def Jokes(c):
    fs = glob.glob("Jokes/" + c + "/*.txt")
    contents = []
    for i, fn in enumerate(fs):
        name = os.path.split(fn)[-1].replace(".txt", "")
        f = open(fn)
        Jokes = f.read()
        f.close()
        contents.append((name, Jokes, i))
    return render_template("Jokes.html", cs=contents)

