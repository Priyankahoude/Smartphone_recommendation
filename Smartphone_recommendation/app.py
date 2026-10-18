from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("Smartphone_cleaned.csv")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)