from flask import Flask, render_template, request, flash, url_for, redirect
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567ONLINESTORE'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=["GET","POST"])
def index():
    files = os.listdir('./static/store_img')
    count = len(files)
    return render_template('index.html', files=files, count=count)

@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        return redirect(url_for('details'))
    return render_template('order.html')

@app.route("/upload", methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT,'order_images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("files"):
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

@app.route("/stores", methods=["GET","POST"])
def stores():
    target1 = os.path.join(APP_ROOT,'static/store_img/')
    target2 = os.path.join(APP_ROOT,'static/owner_img/')

    if not os.path.isdir(target1):
        os.mkdir(target1)
    if not os.path.isdir(target2):
        os.mkdir(target2)

    for file1 in request.files.getlist("store_image"):
        for file2 in request.files.getlist("owner_image"):
            print(file1)
            print(file2)
            filename1 = file1.filename
            filename2 = file2.filename
            if filename1 and filename2 :
                destination1 = "/".join([target1, filename1])
                destination2 = "/".join([target2, filename2])
                file1.save(destination1)
                file2.save(destination2)
                flash("File Uploaded", "success")
                return redirect(url_for('index'))
            else:
                flash("Please attach a file","danger")
                return redirect(url_for('stores'))

    return render_template('stores.html')

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')

@app.route("/search_result", methods=["GET","POST"])
def search_result():
    if request.method == "POST":
        return redirect(url_for('search_result'))
    return render_template('search_result.html')


if __name__ == "__main__":
    app.run(debug=True)
