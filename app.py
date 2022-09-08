from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import storyList

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fruitsmell0374'
debug = DebugToolbarExtension(app)

@app.route('/')
def go_home():
    return render_template('home.html',
                            stories=storyList)

@app.route('/choose-words')
def go_choose_words():
    story_name = request.args['story']
    for story in storyList:
        if story.name == story_name:
            prompts = story.prompts
    return render_template('choose-words.html', prompts=prompts, story=story_name)

@app.route('/story')
def go_story():
    story_name = request.args['story_name']
    for story in storyList:
        if story.name == story_name:
            generated_story = story.generate(request.args)
    return render_template('story.html', generated_story=generated_story)
