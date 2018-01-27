from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lance'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Houston'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The 12 Strong Movie wasas so cool!'
        },
        {
            'author': {'username': 'Pepper'},
            'body': 'Woof Woof Woof'
        },
        {
            'author': {'username': 'Agro'},
            'body': 'Bacon, Bacon, Bacon, Bacon, Sweet Bacon!'
        },
        {
            'author': {'username': 'Sarge'},
            'body': 'Coffee Coffee Coffee!'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
