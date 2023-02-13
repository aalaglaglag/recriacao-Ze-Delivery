
from flask import render_template, Flask
import os

app = Flask(__name__)


@app.route("aalaglaglag/recriacao-Ze-Delivery/settings/pages", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
