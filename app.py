from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("Smartphone_recommendation/Smartphone_cleaned.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    budget = request.form.get("budget")
    brand = request.form.get("brand")

    budget = float(budget)

    filtered_df = df[df['price'] <= budget] 

    if brand:
        filtered_df = filtered_df[
            filtered_df['brand_name'].str.lower() == brand.lower()
        ]

    phones = filtered_df.sort_values(by='rating', ascending=False).head(5)

    return render_template("index.html", phones = phones.to_dict("records"))

if __name__ == "__main__":
    app.run(debug=True)