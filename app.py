from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("home.html")
@app.route('/positions')
def pricing():
    return render_template("positions.html")
@app.route('/services')
def vehicles():
    return render_template("services.html")
@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message);


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
