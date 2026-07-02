from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

# ✅ ADD GALLERY HERE (AFTER app is created)
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# ✅ ONLY ONE RUN (AT END)
if __name__ == "__main__":
    app.run(debug=True)