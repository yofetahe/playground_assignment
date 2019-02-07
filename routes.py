from flask import Flask, render_template

app = Flask("__name__")

@app.route("/play")
def playInitial():
    return render_template("index.html", val=3, col='')

@app.route("/play/<num>")
def playNumber(num):
    return render_template("index.html", val=int(num), col='')

@app.route("/play/<num>/<color>")
def playNumberColor(num, color):
    return render_template("index.html", val=int(num), col=color)

if __name__ == '__main__':
    app.run(debug=True)