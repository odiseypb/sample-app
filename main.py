from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def inicio():
    return render_template('host.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8090)