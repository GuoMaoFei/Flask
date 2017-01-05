from flask import Flask,render_template
from  flask.ext.bootstrap import Bootstrap
from  flask.ext.wtf import  Form
from  wtforms import StringField,SubmitField
from  wtforms.validators import Required

app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='hard to guess string'

@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('index.html',form=form,name=name)

@app.route('/user/<name>')
def user(name):
    return  render_template('user.html',name=name)

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')

if __name__=='__main__':
    app.run(debug=True)