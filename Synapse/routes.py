from flask import Blueprint, render_template, request, redirect, url_for, session,flash


routes = Blueprint('routes', __name__)

@routes.route('/service')
def service():
    
    return render_template('services.html')