from flask import Blueprint, render_template, request
import random


bp = Blueprint(__name__, __name__, template_folder='templates')

def random_string(length=16):
    out_string = ''
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

    for i in range(0, length):
        out_string += chars[random.randint(0, len(chars)-1)]
    
    return out_string


@bp.route('/createnote', methods=['POST', 'GET'])

def show():
    if (request.method == 'POST') and (request.form.get('createnote')):
        #get the text from the text box
        text = request.form.get('notetext')
        #write text to file in notes folder
        while(True):
            try:
                _file = open('noteapp/notes/{}.note'.format(random_string()), 'x' ) 
                _file.write(text)
                _file.close()
                break
            except:
                print("Error!")
                continue

    return render_template('createnote.html')

