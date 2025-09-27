from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola desde Flask 🚀</h1>"

@app.route("/nfc")
def nfc():
    return render_template("landing.html")

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, host="0.0.0.0", port=5000)