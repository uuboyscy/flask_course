from flask import Flask, request
import series as s

app = Flask(__name__)

@app.route('/series')
def series():
    n = int(request.args.get('n'))
    print(n)
    output = str(s.Func(n))
    print(output)
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)