from flask import (Blueprint, url_for, render_template, request)
from . import db
from . import processor as p
from werkzeug.utils import secure_filename
import os


# this should be put in a config file
BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASEDIR, 'upload')
ALLOWED_EXTENSIONS = set(['txt'])

bp = Blueprint('robot', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    response = None
    items = None

    if request.method == 'POST':
        # check if file was uploaded
        if 'file' in request.files and request.files['file'].filename != '':
            uploaded_file = request.files['file']
            if allowed_file(uploaded_file.filename):
                with open(save_file(uploaded_file), 'r') as f:
                    question = f.read()
        else:
            question = request.form['question']
        # job starts
        if question:
            items = p.auto_reply(question)
            if items:
                query = 'SELECT tag, response FROM automated_responses ORDER BY 1'
                data = query_db(query)
                if data:
                    tmp = {r[0]:r[1] for r in data}
                    response = 'No data found'
                    for item in items:
                        if item[0].lower() in tmp:
                            response = tmp[item[0].lower()]
                            break
    return render_template('index.html', title='Home', items=items, reply=response)


def save_file(f):
    f_name = secure_filename(f.filename)
    f.save(os.path.join(UPLOAD_FOLDER, f_name))
    return os.path.join(UPLOAD_FOLDER, f_name)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def query_db(query, args=(), one=False):
    cur = db.get_db().execute(query, args)
    data = cur.fetchall()
    cur.close()
    return (data[0] if data else None) if one else data
