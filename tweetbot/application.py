from flask import Flask

app = Flask(__name__)
#app.config.from_object('HoverSpace.config.DevelopmentConfig')

from tweetbot import views

