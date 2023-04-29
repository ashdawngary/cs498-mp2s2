from flask import Flask, request
from subprocess import Popen
from socket import gethostname, gethostbyname

app = Flask(__name__)

seed = 0
@app.route('/', methods = ['GET'])
def get_seed():
    hn = gethostname()
    return gethostbyname(hn), 200

@app.route('/', methods = ['POST'])
def update_seed():
    process = Popen(['python3', 'stress_cpu.py'])
    return "STARTED", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
