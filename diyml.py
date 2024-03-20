"""
Main application that combines all modules
"""

import os
from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_restful import Api
from authentication import UserAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)


# add apis from other modules
api.add_resource(UserAPI,
                 '/user/<string:user_name>',
                 '/user/<string:user_name>/<string:user_pass>')


### BEGINNING DATA UPLOAD MODULE """"
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg'} # txt temporarily used for testing
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """
    Obtained from https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# note: flask_restful does not support render_template,
# which is why classic flask is used below
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Obtained from https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template('index.html')
    """
    # obtained from https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask?noredirect=1&lq=1
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    """
    Obtained from https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    """
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)


if __name__ == '__main__':
    app.run(debug=True)
