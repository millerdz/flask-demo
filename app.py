from flask import Flask, render_template
import os
import socket

app = Flask(__name__)
secrets = []

@app.route('/')
def hello_world():
    # get the container id
    id = socket.gethostname()

    # get the secrets
    try:
        for entry in os.scandir('/run/secrets'):
            if entry.is_file():
                file = open(entry.path)
                secrets.append(dict([('name', entry.name), ('value', file.read().rstrip())]))
    except FileNotFoundError:
        pass

    return render_template('index.html', id=id, secrets=secrets)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
