from flask import Flask
from flask import render_template
from flask import request
import pickle

big_list = pickle.load(open("scrapers/ChainReactionCycles/ChainReactionCycles.p", "rb"))

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/ara")
def serp():
    query = request.args.get('urun').lower()
    results = filter(lambda x: query in x['name'].lower(), big_list)

    return render_template('serp.html', results = results)

if __name__ == "__main__":
    app.run() 
