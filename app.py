from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        err=HousingException(e,sys)
        logging.info(err)

    logging.info("we are in the main module")
    return "CI-CD established"


if __name__ == "__main__":
    app.run(debug=True)
