from flask import Flask, render_template, request, jsonify
from helpers import predict
import os

application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])


@application.route("/")
def hello():
  return render_template("index.html")

@application.route("/texts", methods=["POST"])
def analyze():
  _text = [request.form['inputText']]
  predictions = predict(_text)
  return render_template("results.html", predictions = predictions)

@application.route("/texts")
def statistics():
  return render_template("statistics.html")

if __name__ == "__main__":
  application.run(host='0.0.0.0')
  application.run()
