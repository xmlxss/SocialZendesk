from flask import render_template, request, jsonify, current_app, redirect, url_for, flash, Response, copy_current_request_context
from app.main import main
from app.services.webhook_service import process_zendesk_webhook
from app.services.sse_service import generate_sse_events
from app.utils.auth_utils import validate_token
from app import db, bcrypt
from app.models import User, WebhookEvent, Survey
from app.forms.registration_form import RegistrationForm
from app.forms.login_form import LoginForm
from flask_login import login_user, logout_user, current_user

@main.route('/')
def home():
    if not current_user.is_authenticated:
        flash('You need to log in to access this page', 'warning')
        return redirect(url_for('main.login'))

    received_webhook_events = WebhookEvent.query.order_by(WebhookEvent.received_at.desc()).limit(10).all()
    sent_surveys = Survey.query.order_by(Survey.id.desc()).limit(10).all()

    return render_template('home.html', received_webhook_events=received_webhook_events, sent_surveys=sent_surveys)


@main.route('/sse_feed')
def sse_feed():
    last_event_id = request.args.get('last_event_id', 0, type=int)
    last_survey_id = request.args.get('last_survey_id', 0, type=int) 
    return generate_sse_events(last_event_id, last_survey_id)  




@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main.route('/webhook/zendesk', methods=['POST'])
def zendesk_webhook():
    if request.method != 'POST':
        return jsonify({'message': 'Method not allowed'}), 405
    if not validate_token(request.headers.get('Authorization')):
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.json.get('ticket')
    if not data:
        return jsonify({'message': 'Invalid payload'}), 400
    return process_zendesk_webhook(data)
    
