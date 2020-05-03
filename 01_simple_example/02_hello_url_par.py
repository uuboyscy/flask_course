from flask import Flask

app = Flask(__name__)

@app.route('/helloFlask')
def helloFlask():
    return 'Hello Flask!'

@app.route('/helloFlask/Allen')
def helloUser_Allen():
    return 'Hello Allen !!!'
@app.route('/helloFlask/Ted')
def helloUser_Ted():
    return 'Hello Ted !!!'
@app.route('/helloFlask/Jack')
def helloUser_Jack():
    return 'Hello Jack !!!'


@app.route('/helloFlask/<username>')
def helloUser(username):
    return 'Hello {} !!!!!!'.format(username)

@app.route('/helloFlask/<username>/<age>')
def userInfo(username, age):
    return 'Hello {}, you are {} years old!'.format(username, age)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)