'''
Take a look at the part4.html to see how to use the CSS
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("part3_2.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)