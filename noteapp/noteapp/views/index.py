from flask import Blueprint, render_template
import glob

bp = Blueprint(__name__, __name__, template_folder='templates')

def fetch_notes():
    note_contents = []
    notes = glob.glob('noteapp/notes/*.note')
    for note in notes:
        with open(note, 'r') as _file:
            note_contents.append(_file.read())
        _file.close()
    return note_contents

@bp.route('/')
def show():
    return render_template('index.html', notes=fetch_notes())

