from flask import Flask, render_template, request
import requests
from apis import sl, chuck
# SL Realtidsinformation 4 API-nyckel : 016287db39614ed1a91365891e96af11
# SL Platsuppslag API-nyckel : cb7a1ff961c54723a59297b51ba0e87f

app = Flask(__name__)

@app.route('/weather')
def weather():
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Stockholm,se&appid=7e2e6f241ccc55c7ab4914d416f2eea7')
    return




@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
