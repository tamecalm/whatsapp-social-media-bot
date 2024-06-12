from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models import User, Post, Analytics
from app.utils import handle_message, schedule_post

bp = Blueprint('routes', __name__)

@bp.route('/webhook', methods=['POST'])
def webhook():
    message = request.form.get('Body')
    sender = request.form.get('From')

    response_message = handle_message(message, sender)
    
    response = MessagingResponse()
    response.message(response_message)

    return str(response)

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@bp.route('/schedule_post', methods=['GET', 'POST'])
def schedule_post_route():
    if request.method == 'POST':
        content = request.form.get('content')
        time = request.form.get('time')
        if content and time:
            schedule_post(time, content)
            flash('Post scheduled successfully', 'success')
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Failed to schedule post', 'danger')
    return render_template('schedule_post.html')

@bp.route('/analytics')
def analytics():
    # Fetch and render analytics data
    analytics_data = Analytics.query.all()
    return render_template('analytics.html', analytics_data=analytics_data)

@bp.route('/recommendations')
def recommendations():
    # Fetch and render content recommendations
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    return render_template('recommendations.html', recommendations=recommendations)
