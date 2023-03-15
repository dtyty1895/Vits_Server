from flask import Flask, send_file, render_template, request
from chat.ChatWaifuCN import generateSound, PlaySound
from flask import make_response
app = Flask(__name__)


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.form.keys()
    data = [i for i in data][0]
    print('Received data:', data)
    save = generateSound("[ZH]"+data+"[ZH]")
    # PlaySound(r'.\output.wav', flags=1)
    return save


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output.wav')
def download_file():
    return send_file('output.wav')

if __name__=='__main__':
    app.debug = True
    app.run()