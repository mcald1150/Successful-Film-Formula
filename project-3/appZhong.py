# import necessary libraries
import pandas as pd
import json

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DA")
def da():
    return render_template("DA.html")

@app.route("/moviesData")
def moviesData():
    df = pd.read_csv('DataSet/movies_metadata.csv')
    movies_data = df.to_dict(orient='records')
    return jsonify(movies_data)

if __name__ == "__main__":
    app.run(debug=True)