from flask import Blueprint, render_template, request, url_for, redirect
main = Blueprint('main', __name__)

# @main.route('/')
# def error_page():
#     return render_template('error-signin.html')

@main.route('/syncing')
def syncing():
    return render_template('syncing.html')

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500