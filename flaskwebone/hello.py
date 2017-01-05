from flask import Flask,render_template,session,redirect,url_for,flash
from  flask.ext.bootstrap import Bootstrap
from  flask.ext.wtf import  Form
from  wtforms import StringField,SubmitField
from  wtforms.validators import Required
import os
from flask.ext.sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name !=form.name.data:
            flash('Looks like you have changed your name')
        session['name']=form.name.data
        return  redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return  render_template('user.html',name=name)

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')

if __name__=='__main__':
    app.run(debug=True)