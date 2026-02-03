from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from AWS!</h1><h2>CI/CD is working!</h2><h3>Your configure the elastic beanstalk correclty"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    # Local development only
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
