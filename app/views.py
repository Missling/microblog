from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])

def login():
  # imported LoginForm class, instantiated an object from it, and sent it down to the template
  form = LoginForm() 

  # validate_on_submit is called as part of a form submission request, it will gather all the data, run all the validators attached to fields, and if everything is all right it will return True, indicating that the data is valid and can be processed.
  if form.validate_on_submit():
    flash('Login requested for OpenID="%s", remember_me=%s' %
      (form.openid.data, str(form.remember_me.data)))
    return redirect('/index')
  return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

    
