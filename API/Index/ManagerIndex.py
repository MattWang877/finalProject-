from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerIndex = Blueprint('ManagerIndex', __name__)


@ManagerIndex.route(r'/ManagerIndex')
@cross_origin()
def manager_index_page():
    if session.get('Login') == 'Login':
        return render_template('/Index/ManagerIndex.html')
    else:
        return redirect(url_for('Login.login_page'))
