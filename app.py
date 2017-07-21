from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    id=socket.gethostname()
    return render_template('index.html', id=id)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
