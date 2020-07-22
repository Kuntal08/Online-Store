from flask import Flask, render_template, request, flash, url_for, redirect
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567ONLINESTORE'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        return redirect(url_for('details'))
    return render_template('order.html')

@app.route("/upload", methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT,'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        if filename :
            destination = "/".join([target, filename])
            file.save(destination)
            flash("File Uploaded", "success")
            return redirect(url_for('details'))
        else:
            flash("Please attach a file","danger")
            return redirect(url_for('upload'))

    return render_template("upload.html")

@app.route("/details", methods=["GET","POST"])
def details():
    if request.method == "POST":
        flash("Order has been placed", "success")
        return redirect(url_for('index'))
    return render_template('details.html')


if __name__ == "__main__":
    app.run(debug=True)
