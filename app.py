
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/home')
def home_page():
    """show home page"""
    return render_template('home.html')


@app.route('/hello/<username>')
def say_hello(username):
    return render_template('hello.html')


@app.route('/add-comment')
def add_comment_form():
    return """
  <h1>Add Comment</h1>
  <form method='POST'>
    <input type='text' placeholder='comment' name='comment'/>
    <button>Submit</button>
  </form>
  """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    return f"""
  <h1>'{comment}' Saved</h1>
  """


@app.route('/form')
def show_form():
    return render_template('form.html')


compliments = ['cool', 'nice', 'awesome', 'beautiful']


@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')


@app.route('/greet')
def get_greet():
    username = request.args["username"]
    msg = choice(compliments)
    return render_template('greet.html', username=username, compliment=msg)


@app.route('/greet-2')
def get_greet_2():
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    nice_compliments = sample(compliments, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants_compliments, compliments=nice_compliments)


@app.route('/lucky')
def show_lucky_num():
    num = randint(1, 5)
    return render_template('hello.html', luck_num=num)


@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word.upper())
