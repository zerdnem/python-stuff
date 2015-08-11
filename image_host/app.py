#!/usr/bin/env python

from flask import Flask, url_for, render_template, request, redirect, abort, session, g, flash, send_from_directory
from werkzeug import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'notactuallysecret'
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
# Set the folder for uploads
ext = set(['png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flist = request.files.getlist("file[]")
        for f in flist:
            if f.filename.rsplit('.', 1)[1] in ext:
                named = uuid.uuid4().hex+'.'+secure_filename(f.filename.rsplit('.', 1)[1])
                f.save('./uploads/' + named)
                flash('It has been uploaded: '+request.url_root+'uploads/'+named, "green")
            else:
                flash('It needs to be an image!', 'red')
    return render_template('index.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.route('/uploads/<path:path>')
def send_js(path):
    return send_from_directory('uploads', path)

if __name__ == "__main__":
    app.run(host='192.168.254.105', port=8080, debug=True, threaded=True)
