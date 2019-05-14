from flask import Flask, render_template, request
from apis import (sl, chuck, time, Weather, Debaser)
import requests
from decimal import Decimal

app = Flask(__name__)


@app.route('/')
def index():
    debaser = Debaser()
    weather = Weather()
    timedate = time()
    sls = sl()

    return render_template('index.html', debaser = debaser, weather = weather,
                            timedate = timedate, sls = sls)

if __name__ == '__main__':
    app.run(debug = True)
#{{sl[0]['TrainNumber']}}
