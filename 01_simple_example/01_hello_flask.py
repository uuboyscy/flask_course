from flask import Flask

app = Flask(__name__)

@app.route('/helloFlask')
def helloFlask():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)