
from flask import render_template, Flask
import os

app = Flask(__name__)

if __name__== 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)
    

def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
