from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return '<h1>Hello from AWS!</h1><p>CI/CD is working!</p>'

@application.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8080)