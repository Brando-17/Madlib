from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtention
from stories import story

app = Flask(__name__)
app.config['Secret_Key'] = "secret"

debug = DebugToolbarExtention(app)

@app.route("/")
def questions():
    prompt = story.prompt
    return render_template("questions.html", prompt=prompt)

@app.route("/story")
def show_story():
    text = story.generate(request.args)
    return render_template("story.html", text = text)