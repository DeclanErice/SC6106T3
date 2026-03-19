from flask import Flask,render_template,request
import os

# serve static files from the `static/` directory
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/transferMoney",methods=["GET","POST"])
def transferMoney():
    return(render_template("transferMoney.html"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)