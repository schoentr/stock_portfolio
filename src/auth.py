from flask import render_template, flash, redirect,url_for,session,abort,g
from .models import User, db
from .forms import AuthForm
from . import app
import functools



def login_required(view):
    """View function decorator.  Restrics acces to decorated rout if user(g.user) not found the 404
    """
    @functools.wraps(view)
    def wrapped_view(**kwags):
        if g.user is None:
            # import pdb; pdb.set_trace()
            abort(404)
        return view(**kwags)
    return wrapped_view

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user=None
    else:
        g.user=User.query.get(user_id)

@app.before_request
def load_logged_in_user():
    """
    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user=User.query.get(user_id)

@app.route('/register',methods=['GET','POST'])
def register():
    """
    """
    form= AuthForm()
    if form.validate_on_submit():
        email= form.data['email']
        password= form.data['password']
        error=None

        if not email or not password:
            error ='Invalid email or password'
        if User.query.filter_by(email=email).first() is  not None:
            error= f'{ email } has already been registered.'
        if error is None:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Registration coplete. Please log in.')
            return redirect(url_for('.login'))
        flash(error)
    return render_template('auth/register.html', form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    form = AuthForm()
    if form. validate_on_submit():
        email= form.data['email']
        password= form.data['password']
        error=None
        user=User.query.filter_by(email=email).first()
        if user is None or not User.check_password_hash(user,password):
            error= 'Invalid username or password.'
        if error is None:
            session.clear()
            session['user_id']= user.id
            return redirect(url_for('.company_detail'))
        flash(error)
    return render_template('auth/login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    """
    """
    session.clear()
    flash('You have been logged out!')
    return redirect(url_for('.login'))

