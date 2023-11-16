from flask import Flask, render_template, request, redirect, url_for
import redis
import os
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
db = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)

@app.route('/')
def index():
    todos = {k.decode(): v.decode() for k, v in db.hgetall('todos').items()}
    
    base_pod = f"{os.environ.get('HOSTNAME', 'unknown')}"
    response = requests.get('http://recommender/hello')

    condition = False
    response_text = "n/a"

    if response.status_code == 200:
        condition = True
        data = response.json()
        
        response_pod = data['pod']
        response_text = data['body']

    return render_template('index.html', todos=todos, base_pod=base_pod, response_pod=response_pod, response_text=response_text, condition=condition)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        db.hset('todos', todo, 0)
    return redirect(url_for('index'))

@app.route('/complete/<todo>')
def complete(todo):
    db.hset('todos', todo, 1)
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    db.delete('todos')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
