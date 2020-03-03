#!/usr/bin/env python3

from flask import Flask, jsonify
import datetime


app = Flask(__name__)


@app.route('/temperature_sensor', methods=['GET'])
def temperature_sensor():
    (t, h) = get_temperature()
    dic = {
        'temperature': t,
        'humidity': h
    }
    dic2 = {
        'timestamp': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'value': dic
    }
    return jsonify(dic2)


def get_temperature():
    return 25.0, 55.0


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
