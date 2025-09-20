from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

def get_counter():
    try:
        with open('/data/counter.txt', 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def update_counter():
    counter = get_counter() + 1
    with open('/data/counter.txt', 'w') as f:
        f.write(str(counter))
    return counter

@app.route('/')
def index():
    counter = update_counter()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', counter=counter, current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)