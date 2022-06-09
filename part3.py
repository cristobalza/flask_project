'''
In `part3.py` application, we have created a templates directory
containing an HTML file called `home.html`. Then, in the application
 module, `part3.py`, we first import the render_template function in 
 **line 1**. Then, the view function home() renders the home.html 
 template by passing its name to render_template() and returning
  the output in **line 6**.
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("part3.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)