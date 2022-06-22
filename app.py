from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Starting machine learning project. This is a simple flask app"


if __name__ == "__main__":
    app.run(debug=True)
