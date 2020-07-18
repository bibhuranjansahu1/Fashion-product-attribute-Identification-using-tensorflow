import model
import output
import pandas as pd
import os
import PIL
#from waitress import serve
from flask import  render_template, request, redirect, url_for,  Blueprint, Flask
#Set root directory
from werkzeug import secure_filename
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#Call your model
#att = output.attributes(path)

bp  = Blueprint('fashion', __name__)
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', )

#Define upload function
@app.route("/uploadUp", methods=["POST"])
def uploadUp():

    upload_dir = os.path.join(APP_ROOT, "uploads/")

    if not os.path.isdir(upload_dir):
        os.mkdir(upload_dir)

    for img in request.files.getlist("file"):
        img_name = img.filename
        destination= "/".join([upload_dir, img_name])

        img.save(destination)

    result=output.up_Attributes(os.path.join(upload_dir, img_name))

    return render_template('your_url.html',  tables=[result.to_html(classes='data', header="true")])
@app.route("/uploadBot", methods=["POST"])
def uploadBot():

    upload_dir = os.path.join(APP_ROOT, "uploads/")

    if not os.path.isdir(upload_dir):
        os.mkdir(upload_dir)

    for img in request.files.getlist("file"):
        img_name = img.filename
        destination= "/".join([upload_dir, img_name])

        img.save(destination)

    result=output.bot_Attributes(os.path.join(upload_dir, img_name))

    return render_template('your_url.html',  tables=[result.to_html(classes='data', header="true")])

if __name__ == "__main__":
	#app.run()
    app.run(host='0.0.0.0',debug=True)
