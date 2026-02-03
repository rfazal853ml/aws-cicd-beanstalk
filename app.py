from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from AWS!</h1><p>CI/CD is working!</p>'

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/health1')
def health1():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
