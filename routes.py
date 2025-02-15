from flask import Blueprint, render_template, flash, request, redirect, url_for

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html') # can also pass show_nav_bar = True, as an arg and it will work

