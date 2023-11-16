from flask import Flask, render_template, request, redirect, url_for
import redis
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
db = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
pod = f"{os.environ.get('HOSTNAME', 'unknown')}"

@app.route('/')
def index():
    todos = {k.decode(): v.decode() for k, v in db.hgetall('todos').items()}
    return render_template('index.html', todos=todos, pod=pod)

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
