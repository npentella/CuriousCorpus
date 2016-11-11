from flask import Flask, render_template, request, jsonify
from helpers import predict, svm_predict_all


application = Flask(__name__)

# svm_prediction = svm_predict_all()


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
  # svm_prediction = svm_predict_all()
  return render_template("statistics.html")

if __name__ == "__main__":
  application.run()
