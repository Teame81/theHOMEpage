from flask import Flask, render_template, request
from apis import (sl, chuck, time, Weather, Debaser,nasa)
import requests
from decimal import Decimal

app = Flask(__name__)


@app.route('/')
def index():
    debaser = Debaser()
    weather = Weather()
    timedate = time()
    sls = sl()
    chuckJoke = chuck()
    nasaPic = nasa()
    return render_template('index.html', debaser = debaser, weather = weather,
                            timedate = timedate, sls = sls, chuckJoke = chuckJoke,
                            nasaPic = nasaPic)

if __name__ == '__main__':
    app.run(debug = True)
#{{sl[0]['TrainNumber']}}
