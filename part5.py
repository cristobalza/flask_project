from flask import Flask, render_template
from flask import request
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}

@app.route("/")
def home():
    return render_template("part5_home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("part5_login.html", form = form)

    # if request.method == "POST":
    #     email = request.form['email']
    #     password = request.form['password']
        
    #     if email in users.keys() and password == users[email]:
    #         return render_template("part5_login.html", message="Success on logging in!")
    #     else:
    #         return render_template("part5_login.html", message="No user with this email or incorrect password.")
    # return render_template("part5_login.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)