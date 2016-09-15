from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('main.html')
    except Exception as e:
        return(str(e))


@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run()