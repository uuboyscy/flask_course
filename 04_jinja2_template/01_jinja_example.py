from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/hello_post2', methods=['GET', 'POST'])
def hello_post2():
    if request.method == 'GET':
        return render_template('hello_post.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        return render_template('hello_post.html',
                               username=username,
                               request_method='post')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
