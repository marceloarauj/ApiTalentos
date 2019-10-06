import subprocess
import sys

subprocess.call([sys.executable,"-m","pip","install","gunicorn"])
subprocess.call([sys.executable,"pip","install","requirements.txt"])

from flask import Flask
app = Flask(__name__)

@app.route("/api/Sports/list")
def hello():
    return "[{'name': ' Atletismo - Arremesso de Peso ','id':1},{'name': ' Atletismo - Corrida de Velocidade ','id':2},{'name': ' Atletismo - Corrida de Fundo ','id':3},{'name': ' Atletismo - Corridas de Meio-Fundo','id':4},]"

if __name__ == "__main__":
    app.run(port=7000)