from flask import Flask, jsonify
import requests

app =  Flask(__name__)


@app.route('/currency/<currency_code>', methods=['GET'])
def get_data(currency_code):
    req = requests.get("http://www.floatrates.com/daily/usd.json")
    data = req.json()
    data = { "currency_code": currency_code, "date": data[currency_code]["date"], "rate": data[currency_code]["rate"] }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)