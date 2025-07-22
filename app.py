from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Haii i am shailu"

if __name__=="__main__":
    app.run(debug=True)
