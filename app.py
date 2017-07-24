from flask import Flask, redirect, render_template, request
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    # get the container id
    id = socket.gethostname()

    # get the secrets
    secrets = []
    try:
        for entry in os.scandir('/run/secrets'):
            if entry.is_file():
                file = open(entry.path)
                secrets.append(dict([('name', entry.name), ('value', file.read().rstrip())]))
    except FileNotFoundError:
        pass

    return render_template('index.html', id=id, secrets=secrets)

@app.route('/kill')
def shutdown():
    shutdown_server()
    return redirect('/')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
