import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/get-date")
def get_date():
    response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Tampa&country=United States of America&state=FL&method=2")
    date = response.json() ["data"] ['date'] ['readable'] 
    return jsonify(date=date)

@app.route("/fajr")
def fajr():
    response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Tampa&country=United States of America&state=FL&method=2")
    fajrtime = response.json() ["data"] ["timings"] ["Fajr"]
    return jsonify(fajrtime = fajrtime)


if __name__ == "__main__":
    app.run(debug=True)