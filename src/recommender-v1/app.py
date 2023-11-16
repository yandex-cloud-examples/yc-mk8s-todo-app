from flask import Flask, render_template, jsonify
import os
import random
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

list = [
    "Купить хлеб",
    "Съездить на море",
    "Почитать документацию Yandex Cloud",
    "Установить Kubernetes",
    "Помыть посуду",
    "Заварить чай"
]

@app.route('/hello')
def hello():
    pod = f"{os.environ.get('HOSTNAME', 'unknown')}"
    message = random.choice(list)
    return jsonify(pod=pod, body=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)