from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html') 

@app.route("/hashtag", methods=['POST'])
def hashtag():
    hashtag_text = request.form.get('hashtag', None)
    return redirect(url_for('hello')) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
